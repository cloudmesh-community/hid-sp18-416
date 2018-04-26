#!/bin/sh

# wait for redis server to start
sleep 10

# run Celery worker
su -c "celery -A file_storage_module worker -l info -n worker-fs -Q file_storage"