from celery import Celery
import numpy as np
import json


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)
    
app = Celery('mat_mul_module')
app.config_from_object('celeryconfig')

  
@app.task(name='mat_mul_module.tasks.mat_mul')
def matrix_multiplication(m,n):
    print("Matrix multiplication task started")
    A = np.random.rand(m,n)
    B = np.random.rand(n,m)
    C = np.matmul(A,B)
    return json.dumps(C.tolist(), cls=NumpyEncoder)
