FROM python:3.6

COPY requirements.txt requirements.txt

RUN apt-get update && \
    mkdir app && \
    pip install -r requirements.txt && \
    adduser --disabled-password --gecos '' celeryuser 

COPY ["add_module.py", "celeryconfig.py", "run-add-worker.sh", "/home/celeryuser/"]

WORKDIR /home/celeryuser
