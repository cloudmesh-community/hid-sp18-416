FROM python:3.6

COPY fs-requirements.txt fs-requirements.txt

ENV C_FORCE_ROOT="true"

RUN apt-get update && \
    pip install -r fs-requirements.txt && \
    mkdir /home/user_data/

COPY . /home/celeryworker/

WORKDIR /home/celeryworker