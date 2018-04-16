#!/bin/sh

# wait for redis server to start
sleep 5

# run Celery worker
su -m celeryuser -c "celery -A add_module worker -l info -n worker-add -Q add"
