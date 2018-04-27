# Big Data Reference Architecture using Python Celery

This is the README for my project on building a Big Data Reference Architecture with Python Celery.

You can run and test the architecture using the following commands in the Makefile.

## Prerequisites

You need to install **Docker** in your system which can be done by following the link [here](https://docs.docker.com/install/).

You can install **Docker Compose** in your system using the following command in a Linux environment. 

	sudo pip install docker-compose

For a more thorough installation guide for Docker Compose please check the official Docker documentation [here](https://docs.docker.com/compose/install/#install-compose) as well.

## Run and Test the service

Make sure to follow the order specified below.

1. Invoke the following command to build and run each of the docker containers.
   - ```make docker_compose_build```
2. Invoke the following command to upload an input file.
   - ```make upload_input_file```
3. Invoke the following command to execute K-means algorithm on the input data set.
   - ```make execute_kmeans```
4. Invoke the following command to get the K-means model or cluster centers.
   - ```make get_kmeans_model```
5. Invoke the following command to get the predictions for the given input data set.
   - ```make get_predictions```
6. Invoke the following command to stop the docker containers.
   - ```make docker_compose_stop```
7. Invoke the following command to remove the docker containers.
   - ```make docker_compose_clean```

If you would like to change the input data file, username or job number given to the service (which are given as parameters to the CURL command please modify the Makefile). Also make sure that the input data file is in the current directory.
