from celery import Celery
from pyspark.ml.feature import VectorAssembler
from pyspark import SparkContext
from pyspark.sql import SQLContext
from hdfs import Config
from hdfs import InsecureClient
from pyspark.ml.clustering import KMeans
from file_storage_module import saveModelinHDFS
from file_storage_module import savePredictioninHDFS

import json
import os
import numpy as np
import settings


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


app = Celery('exec_module')
app.config_from_object(settings.CELERY_CONFIG_FILE_NAME)

file_storage_root_path = settings.FILE_STORAGE_ROOT_PATH
client = InsecureClient('http://hadoop:50070', user='root')
sc = SparkContext(appName="file_storage_worker").getOrCreate()
hdfs_file_path = settings.HDFS_FILE_ROOT_PATH

def preprocessData(ip_file_in_hdfs, features_col):
    sqlContext = SQLContext(sc)
    path = '/' + ip_file_in_hdfs
    client.download(path, 'temp.csv', overwrite=True, n_threads=1)
    df = sqlContext.read.csv('temp.csv', header=True)
     
    for col in df.columns:
        if col in features_col:
            df = df.withColumn(col, df[col].cast('float'))
            
    df = df.na.drop()
    
    vecAssembler = VectorAssembler(inputCols=features_col, outputCol="features")
    df_kmeans = vecAssembler.transform(df).select('id', 'features')
    
    return df_kmeans


def makePredictions(df_kmeans, model):
    sqlContext = SQLContext(sc)
    transformed = model.transform(df_kmeans).select('id', 'prediction')
    rows = transformed.collect()
    predictions = sqlContext.createDataFrame(rows)
    
    return predictions.toPandas().set_index('id')


@app.task(name='exec_module.tasks.execute_kmeans')
def executeKmeans(k, username, jobNum, input_file_name, model_file_name, prediction_file_name, features_col):
    file_path_in_hdfs = username + '/' + jobNum + '/'
    ip_file_in_hdfs = file_path_in_hdfs + input_file_name
    df_kmeans = preprocessData(ip_file_in_hdfs, features_col)
    kmeans = KMeans().setK(k).setSeed(1).setFeaturesCol("features")
    model = kmeans.fit(df_kmeans)

    centers = model.clusterCenters()
    model_file_in_hdfs = file_path_in_hdfs + model_file_name
    saveModelinHDFS.apply_async((file_path_in_hdfs, json.dumps(centers, cls=NumpyEncoder), model_file_in_hdfs))
    
    predictions = makePredictions(df_kmeans, model)
    prediction_file_in_hdfs = file_path_in_hdfs + prediction_file_name
    savePredictioninHDFS.apply_async((file_path_in_hdfs, json.dumps(predictions.values.tolist(), cls=NumpyEncoder), prediction_file_in_hdfs))