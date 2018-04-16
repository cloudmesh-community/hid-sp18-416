
# Python Celery Tutorial (Basic and Docker)

## Overview

[abstract goes here]

In this tutorial the capabilities of Python Celery, the Python distributed task queue will be shared. The tutorial is separated into two sections. 

The first section of the tutorial will describe about the basic usage of Python Celery in the Linux environment and the second section of the tutorial will describe about creating a docker cluster of containers shwoing the usage of Python Celery.

## Resources
[Resources list goes here]

## Basic Tutorial 

This section provides a tutorial of Python Celery in a single machine having a Linux environment. Please make sure to follow all the steps in the given order.

### Install Python Celery in Linux

First, make sure to install ```pip``` in your system using the first command. Then by using ```pip``` (by executing the second command) you can install Python Celery. 

    sudo apt install python3-pip
    pip install -U Celery

### A Brief Description of the Components 

This section introduces the three main components related to buidling the distributed architecture in Python Celery. The following subsections describe the three componets broker, worker and client.

#### Broker
The broker acts as the central component through which communication happens. When the client invokes a task a message, in a protocol understandable by the client, is sent to the relevant worker using a queue. The broker then converts the message into a format understandable by the worker and sends it to the worker. A similar process is executed for the response sent by the worker. 

#### Worker
The workers are responsible for executing specific tasks in the system and each worker (or server) can handle one or more tasks. The workers have a capability to execute tasks concurrently using [Eventlet](http://eventlet.net/) or [gevent](http://www.gevent.org/).

#### Client 
The client is responsible for initiaiting the workflow. The client invokes the specific task by importing the specific task via a Python module. 

### Broker

First, you need to install a broker. Python Celery can use different types of brokers but the most supported brokers are RabbitMQ and Redis. You can select and install one of the brokers below. 

##### RabbitMQ

You can install RabbitMQ in Linux using the following command and start the server. 

    sudo apt-get install rabbitmq-server 
    service rabbitmq-server start

##### Redis

You can install and start Redis in Linux via ```pip```. 

    pip install redis

### Worker
Second, you need to write the specific methods that will be acting as the tasks. The first subsection will provide a brief introduction to the tasks, the second subsection will provide insight on the configuration module, the third subsection how to write the specific tasks using Python Celery and the last subsection will show to start the workers. 

#### Introduction to Tasks

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

#### Configuration

You can define a python module named ```celeryconfig``` as follows. This file will contain configurations used by the distributed task queue.

If the message broker is `rabbitmq` you can use the following broker URL and result backend.

`celeryconfig.py`:

	broker_url = 'pyamqp://'
	result_backend = 'rpc://'
	result_persistent = True

If the message broker is `redis` you can use the following broker URL and result backend.

`celeryconfig.py`:

	broker_url = 'redis://localhost:6379/0'
	result_backend = 'rpc://'

#### Define Tasks in Modules

This section describes how you can define the worker modules containing each of the tasks. All modules have a similar template, therefore I will only be describing the ```add_module``` in order to get a clear understanding of the structure.

Firstly, you have to create a Python file named ```add_module.py```. 

	vim add_module.py 

Second, you have to import celery to be able to define the tasks. It should be the first line of your code.
	
	from celery import Celery

Third, you have to create a Celery instance. Here you will be giving a the name of the module (or file) as the first argument when creating the Celery instance. This will allow for the names to be automatically generated when the tasks are defined in the ```__main__``` module.

	app = Celery('add_module')

Next, you need to specify the configuration module (also described in the previous section) in which you defined the broker configurations for Celery.

	app.config_from_object('celeryconfig')

Now you need to define the method that will handle your task. You have to use the ```@app.task``` annotation to specify that this method is a task (execution unit) in the distributed Celery architecture.  You also need to specify a unique name for your task. I have given the name in a format such as 'module name', 'tasks', 'operation'.

	@app.task(name='add_module.tasks.add')
		def add_two_numbers(x, y):
		    return x + y

Now you have completed the ```add_module.py``` file that handles the add task.

[add_module.py](https://github.com/cloudmesh-community/hid-sp18-416/blob/master/tutorial/python_celery/basic_tutorial/add_module.py):

    from celery import Celery

	app = Celery('add_module')
	app.config_from_object('celeryconfig')

	@app.task(name='add_module.tasks.add')
	def add_two_numbers(x, y):
	    return x + y

In a similar manner you can find the modules for the factorial function and matrix multiplication function.

[factorial_module.py](https://github.com/cloudmesh-community/hid-sp18-416/blob/master/tutorial/python_celery/basic_tutorial/factorial_module.py):

    from celery import Celery

	app = Celery('factorial_module')
	app.config_from_object('celeryconfig')


	@app.task(name='factorial_module.tasks.factorial')
	def factorial_of_n(n):
	    result = 1
	    for i in range(1,n+1):
	        result *= i
	    return result

Here in the matrix multiplication module since the output of the matrix multiplication is a matrix (or ndarray) we need to convert it to a format that is understandable by the client. Therefore, the ```NumpyEncoder``` is written such that the method converts a nd array to a list.

[mat_mul_module.py](https://github.com/cloudmesh-community/hid-sp18-416/blob/master/tutorial/python_celery/basic_tutorial/mat_mul_module.py):

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

Finally, you need to add the following configuration to `celeryconfig.py` in order to specify the route defined for each task. Each of the task routes are defined in a manner such that the name of the task is used as a key while the queue which stores the requests are specified as the value in json object. You can find the complete configuration file [here](https://github.com/cloudmesh-community/hid-sp18-416/blob/master/tutorial/python_celery/basic_tutorial/celeryconfig.py).

	task_routes = {
	    'add_module.tasks.add': {'queue':'add'},
	    'mat_mul_module.tasks.mat_mul': {'queue':'mat_mul'},
	    'factorial_module.tasks.factorial': {'queue':'factorial'}
	}

#### Start the Workers

You can use the following commands to start the celery workers. Make sure to execute each of the commands below in separate terminals. The ```-A``` argument defines the name of the module, ```-l``` argument specifies the log level, ```-n``` specifies the name for the server/worker node while ```-Q``` specifies the queue associated with the worker.

    celery -A add_module worker -l info -n worker-add -Q add
    celery -A factorial_module worker -l info -n worker-factorial -Q factorial
    celery -A mat_mul_module worker -l info -n worker-mat-mul -Q mat_mul

### Client

The clients below can be used to invokes the long running and quick tasks. 
 
#### Calling Tasks

Each of the python files have a similar structure. Therefore, I will be only explaining the structure of the ```call_add_task.py``` file.

First, you need to import the specific task from the module. In this case, it would be importing the function ```add_two_numbers``` from the ```add_module```. 

	from add_module import add_two_numbers

Second, you need to apply the task asynchronously by sending a message.

	response = add_two_numbers.apply_async((4,6))

Third, in order to get the result from the response you need to use the following method and print.

	print(response.get())

Now, you have the final ```call_add_task.py``` file which invokes the add task.

[call_add_task.py](https://github.com/cloudmesh-community/hid-sp18-416/blob/master/tutorial/python_celery/basic_tutorial/call_add_task.py):

    from add_module import add_two_numbers

	response = add_two_numbers.apply_async((4,6))
	print(response.get())

In a similar manner you can find the task invocation for the factorial function and matrix multiplication function.

[call_factorial_task.py](https://github.com/cloudmesh-community/hid-sp18-416/blob/master/tutorial/python_celery/basic_tutorial/call_factorial_task.py):

    from factorial_module import factorial_of_n
	
	response = factorial_of_n.apply_async((20000,))
	print(response.get())
	
[call_mat_mul_task.py](https://github.com/cloudmesh-community/hid-sp18-416/blob/master/tutorial/python_celery/basic_tutorial/call_mat_mul_task.py):

    from mat_mul_module import matrix_multiplication

	response = matrix_multiplication.apply_async((20,20))
	print(response.get())

### Makefile

You can find the sample Makefile [here](https://github.com/cloudmesh-community/hid-sp18-416/blob/master/tutorial/python_celery/basic_tutorial/Makefile). You can use the following make commands from the file to test the ```basic_tutorial``` code [here](https://github.com/cloudmesh-community/hid-sp18-416/tree/master/tutorial/python_celery/basic_tutorial).

First, in three separate terminals invoke the following commands.
	
	celery_start_add_worker
	celery_start_factorial_worker
	celery_start_mat_mul_worker

Next, in three seperate terminals (concurrently) invoke the following commands to showcase the functionality of Python Celery.

	make test_add_task
	make test_mat_mul_task
	make test_factorial_task

Finally, once you have completed the tests you can kill the workers using the following command.

	make kill_workers

## Docker Tutorial 


[Docker tutorial goes here]
