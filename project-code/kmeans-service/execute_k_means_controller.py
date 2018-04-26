import connexion
import six

from executor_module import executeKmeans
from swagger_server.models.error import Error  # noqa: E501
from swagger_server import util


def execute_kmeans(k, username, jobNum, prediction_file_name, model_file_name, input_file_name, features_col):  # noqa: E501
    executeKmeans.apply_async((k, username, jobNum, input_file_name, model_file_name, prediction_file_name, features_col))
    return 'started executing KMeans for username ' + username + ' and job number ' + jobNum
