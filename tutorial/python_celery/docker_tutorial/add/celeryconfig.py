broker_url = 'redis://:devpassword@redis:6379/0'
result_backend = 'rpc://'
result_persistent = True
task_routes = {
    'add_module.tasks.add': {'queue':'add'},
    'mat_mul_module.tasks.mat_mul': {'queue':'mat_mul'},
    'factorial_module.tasks.factorial': {'queue':'factorial'}
}
