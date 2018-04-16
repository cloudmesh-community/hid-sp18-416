#!/bin/sh

# wait for redis server to start
sleep 15

# run Celery worker
su -m celeryuser -c "celery -A mat_mul_module worker -l info -n worker-mat-mul -Q mat_mul"
