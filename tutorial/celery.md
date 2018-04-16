
# Python Celery (Basic Tutorial and Docker Tutorial)

## Overview

Celery is an asynchronous task queue which is based upon distributed message passing and uses RabbitMQ or Redis as the communication system. The smallest unit of execution in Python Celery is a task, which can be used to execute either long running or quick tasks. Celery also provides the flexibility to execute tasks synchronously and asynchronously. With the support of Eventlet and gevent, Celery also has the capability to execute tasks concurrently in one or more server/worker nodes. Celery can be understood as a tool that encompasses many communication systems, abstractions, scheduling and real time operation handling capabilities. Celery also provides support for a wide array of configuration options such as task timeouts, retries and task distribution. Celery is a easy to use, highly configurable, flexible and fast tool that can be used to handle a very large amount of tasks of varying nature. 

In this tutorial the capabilities of Python Celery, the Python distributed task queue will be shared. The tutorial is separated into two sections. 

The first section of the tutorial will describe about the **basic usage of Python Celery in the Linux environment** and the second section of the tutorial will describe about **creating a cluster of Docker containers showing the usage of Python Celery in a distributed environment**.

You can find the links for the tutorial structures below.

This tutorial provides an overview of the structure for installing and running Python Celery in a Linux environment.

[Basic Tutorial](https://github.com/cloudmesh-community/hid-sp18-416/tree/master/tutorial/python_celery/basic_tutorial)

If you want to have a quick look at the Docker containers and the invocation of tasks make sure to have Docker and Docker Compose installed beforehand and then invoke the make commands [here](https://github.com/cloudmesh-community/hid-sp18-416/blob/master/tutorial/python_celery/docker_tutorial/Makefile). You can also check the ```Docker Tutorial``` section at the bottom to understand it thoroughly.

[Docker Tutorial](https://github.com/cloudmesh-community/hid-sp18-416/tree/master/tutorial/python_celery/docker_tutorial)

## Resources

http://docs.celeryproject.org/en/latest/

https://www.vinta.com.br/blog/2017/celery-overview-archtecture-and-how-it-works/

https://docs.docker.com/install/#supported-platforms

https://docs.docker.com/compose/install/#install-compose

https://nickjanetakis.com/blog/dockerize-a-flask-celery-and-redis-application-with-docker-compose

## Basic Tutorial 

This section provides a tutorial of Python Celery in a single node having a Linux environment. Please make sure to follow all the steps in the given order.

### Install Python Celery in Linux

First, make sure to install ```pip``` in your system using the first command. Then by using ```pip``` (by executing the second command) you can install Python Celery. 

    sudo apt install python3-pip
    pip install -U Celery

### A Brief Description of the Components 

This section introduces the three main components related to buidling the distributed architecture in Python Celery. The following subsections describe the three componets broker, worker and client.

#### Broker
The broker acts as the central component through which communication happens. When the client invokes a task, a message in a protocol understandable by the client is sent to the relevant worker through a queue. The broker then converts the message into a format understandable by the worker and sends it to the worker. A similar process is executed for the response sent by the worker. 

#### Worker
The workers are responsible for executing specific tasks in the system and each worker (or server) can handle one or more tasks. The workers have a capability to execute tasks concurrently using [Eventlet](http://eventlet.net/) or [gevent](http://www.gevent.org/).

#### Client 
The client is responsible for initiaiting the workflow. The client invokes the specific task by importing the specific task via a Python module. 

### Broker

First, you need to install a broker. Python Celery can use different types of brokers but the most supported are RabbitMQ and Redis. You can select and install one of the brokers below. 

##### RabbitMQ

You can install RabbitMQ in Linux using the following command and start the server. 

    sudo apt-get install rabbitmq-server 
    service rabbitmq-server start

##### Redis

You can install and start Redis in Linux via ```pip```. 

    pip install redis

### Worker
Second, you need to write the specific methods that will be acting as the tasks. The first subsection will provide a brief introduction to the tasks, the second subsection will provide insight on the configuration module, the third subsection will show how to write the specific tasks using Python Celery and the last subsection will show how to start the workers. 

#### Introduction to Tasks

Following are the tasks that will be executed by the Celery workers.
   
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

Third, you have to create a Celery instance. Here you will be giving the name of the module (or file) as the first argument when creating the Celery instance. This will allow for the names to be automatically generated when the tasks are defined in the ```__main__``` module.

	app = Celery('add_module')

Next, you need to specify the name of the configuration module (also described in the previous section) in which you defined the broker configurations for Celery.

	app.config_from_object('celeryconfig')

Now you need to define the method that will handle your task. You have to use the ```@app.task``` annotation to specify that this method is a task (execution unit) in the distributed Celery architecture.  You also need to specify a unique name for your task. I have given the name in a format such as ```module name```, ```tasks```, ```operation```.

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

[mat_mul_module.py](https://github.com/cloudmesh-community/hid-sp18-416/blob/master/tutorial/python_celery/basic_tutorial/mat_mul_module.py):

Here in the matrix multiplication module since the output of the matrix multiplication is a matrix (or ndarray) we need to convert it to a format that is understandable by the client. Therefore, the ```NumpyEncoder``` is written such that the method converts a nd array to a list.


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
	
	make celery_start_add_worker
	make celery_start_factorial_worker
	make celery_start_mat_mul_worker

Next, in three seperate terminals (concurrently) invoke the following commands to showcase the functionality of Python Celery.

	make test_add_task
	make test_mat_mul_task
	make test_factorial_task

Finally, once you have completed the tests you can kill the workers using the following command.

	make kill_workers

## Docker Tutorial 

This section provides a tutorial of Python Celery in a Docker environment creating multiple containers for each of the servers. Please make sure to follow all the steps in the given order.

### Prerequisites

You need to install **Docker** in your system which can be done by following the link [here](https://docs.docker.com/install/).

You can install **Docker Compose** in your system using the following command in a Linux environment. 

	sudo pip install docker-compose

For a more thorough installation guide for Docker Compose please check the official Docker documentation [here](https://docs.docker.com/compose/install/#install-compose) as well.

### Structure of the Modules

Each module ( [add](https://github.com/cloudmesh-community/hid-sp18-416/tree/master/tutorial/python_celery/docker_tutorial/add), [factorial](https://github.com/cloudmesh-community/hid-sp18-416/tree/master/tutorial/python_celery/docker_tutorial/factorial) and [matrix multiplication](https://github.com/cloudmesh-community/hid-sp18-416/tree/master/tutorial/python_celery/docker_tutorial/mat_mul) ) above is defined in a dedicted package structure. Following is the directory structure of the ```add module```, which you can also find [here](https://github.com/cloudmesh-community/hid-sp18-416/tree/master/tutorial/python_celery/docker_tutorial/add).

```
├── add
│   ├── add_module.py
│   ├── celeryconfig.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── run-add-worker.sh
```

In the following sub sections I will describe about each of the files in the package.

#### add_module.py

Firstly, you have to update the module file defined in the previous tutorial. The only addition you have to make to the file is to define the module name with the package name as follows.
	
	app = Celery('add.add_module')
	
You can find the newly updated ```add_module.py``` file [here](https://github.com/cloudmesh-community/hid-sp18-416/blob/master/tutorial/python_celery/docker_tutorial/add/add_module.py).

#### celeryconfig.py

Second, you have to update the configuration file with the new broker backend url. In the previous section we we using the local redis server, therefore we defined the broker URL as follows.

	broker_url = 'redis://localhost:6379/0'

Now we will be defining the new redis server installation (with password support) in a docker container. Therefore, you have to define the broker URL as follows. You can find the newly updated ```celeryconfig.py``` [here](https://github.com/cloudmesh-community/hid-sp18-416/blob/master/tutorial/python_celery/docker_tutorial/add/celeryconfig.py).

	broker_url = 'redis://:devpassword@redis:6379/0'

#### requirements.txt

Now you will be adding this new file which will defines the packages that need to be installed inside the docker container. For the add module you will only need two packages which are defined as follows. You can find the ```requirements.txt``` file for add module [here](https://github.com/cloudmesh-community/hid-sp18-416/blob/master/tutorial/python_celery/docker_tutorial/add/requirements.txt).
	
	redis==2.10.6
	celery==4.1.0

In the matrix mulitiplication module you would additionally need the ```numpy``` module. Therefore for the matrix multiplication module you will need three packages which are defined as follows. You can find the ```requirements.txt``` file for matrix multiplication module [here](https://github.com/cloudmesh-community/hid-sp18-416/blob/master/tutorial/python_celery/docker_tutorial/mat_mul/requirements.txt).

	redis==2.10.6
	celery==4.1.0
	numpy>=1.14.2

#### run-add-worker.sh

In this shell script we will be defining the command to start the celery worker for the add module. Before starting the celery worker we will be waiting for a few seconds until the redis server is started. Here we will be starting the celery worker using a separate user called ```celeryuser``` created for this purpose due to the reason that celery workers should not be started from the super user. 

	#!/bin/sh

	# wait for redis server to start
	sleep 5

	# run Celery worker
	su -m celeryuser -c "celery -A add_module worker -l info -n worker-add -Q add"

#### Dockerfile

Next you need to define the contents of the Dockerfile used to build the worker for the add_module.

The first line specifies the base image which you can pull from dockerhub. We select the ```python``` image with version ```3.6```. 

	FROM python:3.6

Next the ```requirements.txt``` file will be copied to the docker container via the ```COPY``` command.

	COPY requirements.txt requirements.txt

Now the following ```RUN``` command executes a set of commands inside the docker image. 

The following command updates the system.

	apt-get update

The following command installs the necessary requirements from the ```requirements.txt``` file via pip.

	pip install -r requirements.txt

The following command creates a new user to start the celery worker.

	adduser --disabled-password --gecos '' celeryuser

The next ```COPY``` command copies the files specified in the first three arguments in to the folder specified by the fourth argument.

	COPY ["add_module.py", "celeryconfig.py", "run-add-worker.sh", "/home/celeryuser/"]

Finally, the working directory for the image is set via the following command.

	WORKDIR /home/celeryuser

You can find the complete content of the Dockerfile below and [here](https://github.com/cloudmesh-community/hid-sp18-416/blob/master/tutorial/python_celery/docker_tutorial/add/Dockerfile).
		
	FROM python:3.6

	COPY requirements.txt requirements.txt

	RUN apt-get update && \
	    mkdir app && \
	    pip install -r requirements.txt && \
	    adduser --disabled-password --gecos '' celeryuser

	COPY ["add_module.py", "celeryconfig.py", "run-add-worker.sh", "/home/celeryuser/"]

	WORKDIR /home/celeryuser

Both modules ```mat_mul``` and ```factorial``` have a similar directory structure and content for their files. You can find the files for the matrix multiplication module [here](https://github.com/cloudmesh-community/hid-sp18-416/tree/master/tutorial/python_celery/docker_tutorial/mat_mul) and factorial module [here](https://github.com/cloudmesh-community/hid-sp18-416/tree/master/tutorial/python_celery/docker_tutorial/factorial).

### Calling Tasks

Following is the folder structure for creating the containers to invoke the long running/quick tasks.

```
├── call_add_module.py
├── call_add_module.sh
├── call_factorial_module.py
├── call_factorial_module.sh
├── call_mat_mul_module.py
├── call_mat_mul_module.sh
├── celeryconfig.py
├── docker-compose.yml
├── Dockerfile
├── Makefile
└── requirements.txt
```

I will describe about the files necessary to invoke the add task. The content and structure is similar to the matrix multiplicaion and factorial tasks.

#### call_add_module.py

First we define the python file to invoke the Celery task. Compared to the same named python file defined in the previous tutorial this section only requires changes in the import statement due to moving the source code into a package. You can find the file [here](https://github.com/cloudmesh-community/hid-sp18-416/blob/master/tutorial/python_celery/docker_tutorial/call_add_module.py).

	from add.add_module import add_two_numbers

#### call_add_module.sh

Now we define the shell script that will invoke the ```call_add_module.py``` file. We will be introducing a 6 second sleep here as well.

	#!/bin/sh

	sleep 6

	python -m call_add_module

#### requirements.txt

Now we will be defining the requirements file which has the content as follows.

	redis==2.10.6
	celery==4.1.0
	numpy>=1.14.2

#### celeryconfig.py

Similar to the configuration file described in the previous section the only change required here is the inclusion of the password in the broker URL. You will be able to find the config file [here](https://github.com/cloudmesh-community/hid-sp18-416/blob/master/tutorial/python_celery/docker_tutorial/celeryconfig.py).

#### Dockerfile

Now we will be defining the Dockerfile used to create the docker containers for calling the tasks. For simplicity I will be using this same Dockerfile to create the three containers for invoking the three tasks.

Here the ```COPY . code/``` command in Docker copies all the files in the current (.) folder in the host machine into the code folder within the docker container. You can find the Dockerfile [here](https://github.com/cloudmesh-community/hid-sp18-416/blob/master/tutorial/python_celery/docker_tutorial/Dockerfile) and the content below.

	FROM python:3.6

	COPY . code/

	RUN apt-get update && \
	    pip install -r code/requirements.txt && \
	    adduser --disabled-password --gecos '' celeryuser

	WORKDIR code

### docker-compose.yml

We will be using Docker Compose which is a tool for defining and running multi-container **Docker** applications. 

Here I will be describing 3 types of services. One is the **redis** service, another is the **celery-add-worker** service and the last will be the **call-add-module** service. The workers and call services are the same for the matrix multiplication and factorial modules. You can find the complete file [here](https://github.com/cloudmesh-community/hid-sp18-416/blob/master/tutorial/python_celery/docker_tutorial/docker-compose.yml).

#### redis service

The following configuration specifies to pull the Docker image from dockerhub and specifies the command to execute in the beginning of the redis service container (note that we have used the support of passwords as well - the password used here is devpassword). The ```ports``` key specifies the port mapping while the ```volumes``` key specifies the mounted volumes.

	redis:
	  image: 'redis:3.0-alpine'
	  command: redis-server --requirepass devpassword
	  hostname: redis
	  volumes:
	    - 'redis:/var/lib/redis/data'
	  ports:
	    - '6379:6379'
 
 You also need to specify the volumes used in the volumes section as follows.
	
	volumes:
	  redis:

#### celery-add-worker service

The following configuration specifies the build content for the service which contains the Dockerfile inside the package ```add```. We need to also link the redis service using the ```links``` key. We can also specify the dependency between containers with ```depends_on``` key. The ```command``` key specifies the shell script which needs to be run in order to start the Celery worker for the add task when the container gets started.

    celery-add-worker:
	  build:
	    context: add
	    dockerfile: Dockerfile
	  command: ./run-add-worker.sh
	  depends_on:
	    - redis
	  links:
	    - redis

#### call-add-module service

Similar to the description in the above section we define the call-add-module service.

	call-add-module:
	  build:
	    context: .
	    dockerfile: Dockerfile
	  command: ./call_add_module.sh
	  depends_on:
	    - celery-add-worker
	    - redis
	  links:
	    - celery-add-worker
	    - redis 

### Makefile

You can find the Makefile [here](https://github.com/cloudmesh-community/hid-sp18-416/blob/master/tutorial/python_celery/docker_tutorial/Makefile). You can use the following make commands from the file to start and test the ```docker_tutorial``` code [here](https://github.com/cloudmesh-community/hid-sp18-416/tree/master/tutorial/python_celery/docker_tutorial).

First, invoke the following command to build the image, run the container and invoke the add, factorial and matrix multiplication tasks.
	
	make docker_compose_start

Next, once you have completed the tests you can stop the docker containers using the following command.

	make docker_compose_stop

Finally, once you have completed the tests you can clean using the following command.

	make docker_compose_clean
