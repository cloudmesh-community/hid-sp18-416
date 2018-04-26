import connexion
import six

from file_storage_module import getClusterCentersfromHDFS
from swagger_server.models.error import Error  # noqa: E501
from swagger_server import util


def get_kmeans_model(username, jobNum, fileName):  # noqa: E501
    getClusterCentersfromHDFS.apply_async((username, jobNum, fileName))
    return 'started getting the KMeans model for username ' + username + ' job number ' + jobNum + ' into ' + fileName 
