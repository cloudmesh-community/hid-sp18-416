FROM python:3.6

COPY requirements.txt requirements.txt

RUN apt-get update && \
    pip install -r requirements.txt && \
    adduser --disabled-password --gecos '' celeryuser 

COPY ["factorial_module.py", "celeryconfig.py", "run-factorial-worker.sh", "/home/celeryuser/"]

WORKDIR /home/celeryuser
