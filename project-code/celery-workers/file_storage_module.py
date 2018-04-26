# Module that interacts with HDFS
from celery import Celery
from hdfs import Config
from numpy import array
from hdfs import InsecureClient

import os
import numpy as np
import json
import settings
import shutil

app = Celery('fs_module')
app.config_from_object(settings.CELERY_CONFIG_FILE_NAME)

file_storage_vol_path = settings.FILE_STORAGE_VOL_PATH
file_storage_root_path = settings.FILE_STORAGE_ROOT_PATH
client = InsecureClient('http://hadoop:50070', user='root')


@app.task(name='fs_module.tasks.save_input_file')
def saveInputFileinHDFS(username, jobNum, input_file_name):
    ip_file_path = username + '/' + jobNum
    ip_file_path_in_fs = file_storage_root_path + ip_file_path
    ip_file_in_hdfs = '/' + ip_file_path + '/' + input_file_name
    ip_file_in_fs = ip_file_path_in_fs + '/' + input_file_name

    if (not os.path.exists(ip_file_path_in_fs)):
        os.makedirs(ip_file_path_in_fs, 0o755)
    shutil.move(file_storage_vol_path + ip_file_path + "/" + input_file_name, ip_file_in_fs)
    client.upload(ip_file_in_hdfs, ip_file_in_fs, overwrite=False, n_threads=1)

    return 'saved input file ' + input_file_name + ' in hdfs'


@app.task(name='fs_module.tasks.save_model')
def saveModelinHDFS(fp_in_hdfs, centers, model_file_in_hdfs):
    centers_arr = array(json.loads(centers))
    local_file =  "temp_model.txt"
    model_file_in_fs = file_storage_root_path + fp_in_hdfs + local_file
    np.savetxt(model_file_in_fs, centers_arr)
    client.upload('/' + model_file_in_hdfs, model_file_in_fs, overwrite=False, n_threads=1)
    os.remove(model_file_in_fs)


@app.task(name='fs_module.tasks.save_predictions')
def savePredictioninHDFS(fp_in_hdfs, predictions, prediction_file_in_hdfs):
    predictions_arr = array(json.loads(predictions))
    local_file =  "temp_prediction.txt"
    prediction_file_in_fs = file_storage_root_path + fp_in_hdfs + local_file
    np.savetxt(prediction_file_in_fs, predictions_arr)
    client.upload('/' + prediction_file_in_hdfs, prediction_file_in_fs, overwrite=False, n_threads=1)
    os.remove(prediction_file_in_fs)


@app.task(name='fs_module.tasks.get_model')
def getClusterCentersfromHDFS(username, jobNum, model_file_name):
    model_file_path = username + '/' + jobNum + '/'
    local_file_name = "model.txt"
    model_file_in_fs = file_storage_root_path + model_file_path + local_file_name
    model_file_in_hdfs = '/' + model_file_path + model_file_name
    if (not os.path.exists(file_storage_root_path + model_file_path)):
        os.makedirs(file_storage_root_path + model_file_path, 0o755)

    client.download(model_file_in_hdfs, model_file_in_fs, n_threads=5)
    shutil.move(model_file_in_fs, file_storage_vol_path + model_file_path + "/" + model_file_name)
    

@app.task(name='fs_module.tasks.get_predictions')
def getPredictionsfromHDFS(username, jobNum, prediction_file_name):
    prediction_file_path = username + '/' + jobNum + '/'
    local_file_name = "prediction.txt"
    prediction_file_in_fs = file_storage_root_path + prediction_file_path + local_file_name
    prediction_file_in_hdfs = '/' + prediction_file_path + prediction_file_name
    if (not os.path.exists(file_storage_root_path + prediction_file_path)):
        os.makedirs(file_storage_root_path + prediction_file_path, 0o755)

    client.download(prediction_file_in_hdfs, prediction_file_in_fs, n_threads=5)
    shutil.move(prediction_file_in_fs, file_storage_vol_path + prediction_file_path + "/" + prediction_file_name)
