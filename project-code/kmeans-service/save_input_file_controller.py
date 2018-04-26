import connexion
import six

from file_storage_module import saveInputFileinHDFS
from swagger_server.models.error import Error  # noqa: E501
from swagger_server import util


def save_input_file(username, jobNum, fileName):  # noqa: E501
    saveInputFileinHDFS.apply_async((username, jobNum, fileName))
    return 'started save for input file ' + fileName + ' for user ' + username + ' and job number ' + jobNum  
