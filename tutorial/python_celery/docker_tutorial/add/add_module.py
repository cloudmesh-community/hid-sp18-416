from celery import Celery
    
app = Celery('add.add_module')
app.config_from_object('celeryconfig')

    
@app.task(name='add_module.tasks.add')
def add_two_numbers(x, y):
    print("Add task started")
    return x + y
