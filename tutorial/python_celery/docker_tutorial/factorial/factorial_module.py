from celery import Celery
    
app = Celery('factorial_module')
app.config_from_object('celeryconfig')

   
@app.task(name='factorial_module.tasks.factorial')
def factorial_of_n(n):
    print("Factorial task started")
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
