#!/bin/sh

# wait for redis server to start
sleep 10

# run Celery worker
su -m celeryuser -c "celery -A factorial_module worker -l info -n worker-factorial -Q factorial"
