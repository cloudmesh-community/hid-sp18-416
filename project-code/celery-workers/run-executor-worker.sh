#!/bin/sh

# wait for redis server to start
sleep 10

# run Celery worker
su -c "celery -A executor_module worker -l info -n worker-exec -Q executor"