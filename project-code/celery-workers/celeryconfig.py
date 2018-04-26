broker_url = 'redis://:devpassword@redis:6379/0' # for redis
result_backend = 'rpc://'
result_persistent = True
task_routes = {
    'fs_module.tasks.save_input_file': {'queue':'file_storage'},
    'fs_module.tasks.save_model': {'queue':'file_storage'},
    'fs_module.tasks.save_predictions': {'queue':'file_storage'},
    'fs_module.tasks.get_model': {'queue':'file_storage'},
    'fs_module.tasks.get_predictions': {'queue':'file_storage'},
    'exec_module.tasks.execute_kmeans': {'queue':'executor'}
}