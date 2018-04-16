FROM python:3.6

COPY . code/

RUN apt-get update && \
    pip install -r code/requirements.txt && \
    adduser --disabled-password --gecos '' celeryuser 

WORKDIR code
