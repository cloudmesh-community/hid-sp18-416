celery_start_add_worker:
	celery -A add_module worker -l info -n worker-add -Q add

celery_start_factorial_worker:
	celery -A factorial_module worker -l info -n worker-factorial -Q factorial

celery_start_mat_mul_worker:
	celery -A mat_mul_module worker -l info -n worker-mat-mul -Q mat_mul

test_add_task:
	python call_add_task.py

test_mat_mul_task:
	python call_mat_mul_task.py

test_factorial_task:
	python call_factorial_task.py

kill_workers:
	pkill -9 -f 'worker-mat-mul'
	pkill -9 -f 'worker-add'
	pkill -9 -f 'worker-factorial'
