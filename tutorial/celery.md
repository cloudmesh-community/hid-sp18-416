
# Python Celery Tutorial


Install Python-Celery in Linux (open terminal in virtual environment)

    pip install -U Celery

## Components 

There are three main components related to a distributed architecture in Python Celery. Namely,

 - Broker
 - Worker
 - Client 

## Broker

Installation of message brokers are as follows. You can select and install one of the message brokers below. Execute the following commands in a virtual environment.

#### Rabbit MQ

    sudo apt-get install rabbitmq-server 
    service rabbitmq-server start

#### Redis

    pip install redis

## Worker

### Introduction to Tasks

Following are the tasks that will be executed by Celery workers.
   
##### Task 1
  Follwing is a simple, quick and fast function to add two numbers.
  
    def add(x, y):
        return x + y
    
##### Task 2
Following is a function to calculate the factorial of a given number. Due to the for loop, given a large number this function can be resource intensive.
    
    def factorial(n):
        result = 1
        for i in range(1,n+1):
            result *= i
        return result

 
##### Task 3
    
Following is a function to perform the multiplication of two matrices. Given that the matrices are sufficiently large the following function can be resource intensive.
    
    def matrix_multiplication(m,n):
        A = np.random.rand(m,n)
        B = np.random.rand(n,m)
        C = np.matmul(A,B)
        return C

### Configuration

You can define a python module named ```celeryconfig``` as follows. This file will contain configurations used by the distributed task queue.

If the message broker is `rabbitmq` use the following broker URL and result backend.

`celeryconfig.py`:

	broker_url = 'pyamqp://'
	result_backend = 'rpc://'
	result_persistent = True


If the message broker is `redis` use the following broker URL and result backend.

`celeryconfig.py`:

	broker_url = 'redis://localhost:6379/0'
	result_backend = 'rpc://'

### Define Tasks in Modules

`add_module.py`:

    from celery import Celery

	app = Celery('add_module')
	app.config_from_object('celeryconfig')

	@app.task(name='add_module.tasks.add')
	def add_two_numbers(x, y):
	    return x + y

`factorial_module.py`:

    from celery import Celery

	app = Celery('factorial_module')
	app.config_from_object('celeryconfig')


	@app.task(name='factorial_module.tasks.factorial')
	def factorial_of_n(n):
	    result = 1
	    for i in range(1,n+1):
	        result *= i
	    return result


`mat_mul_module.py`:

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
	    A = np.random.rand(m,n)
	    B = np.random.rand(n,m)
	    C = np.matmul(A,B)
	    return json.dumps(C.tolist(), cls=NumpyEncoder)


Add the following configuration to `celeryconfig.py` in order to specify the route defined for each task.

	task_routes = {
	    'add_module.tasks.add': {'queue':'add'},
	    'mat_mul_module.tasks.mat_mul': {'queue':'mat_mul'},
	    'factorial_module.tasks.factorial': {'queue':'factorial'}
	}


### Start the Workers

Execute the following commands in different terminals in the same virtual environment.

    celery -A add_module worker -l info -n worker-add -Q add
    celery -A factorial_module worker -l info -n worker-factorial -Q factorial
    celery -A mat_mul_module worker -l info -n worker-mat-mul -Q mat_mul

## Client

The client below invokes long running and quick tasks.
 
### Calling Tasks

`call_modules.py`:

    from add_module import add_two_numbers
	from factorial_module import factorial_of_n
	from mat_mul_module import matrix_multiplication

	response = factorial_of_n.apply_async((20000,))
	print(response.get())
	response = matrix_multiplication.apply_async((20,20))
	print(response.get())
	response = add_two_numbers.apply_async((4,6))
	print(response.get())
