import connexion
import six

from file_storage_module import getPredictionsfromHDFS
from swagger_server.models.error import Error  # noqa: E501
from swagger_server import util


def get_predictions(username, jobNum, fileName):  # noqa: E501
    getPredictionsfromHDFS.apply_async((username, jobNum, fileName))
    return 'started getting predictions for username ' + username + ' job number ' + jobNum + ' and saving into ' + fileName
