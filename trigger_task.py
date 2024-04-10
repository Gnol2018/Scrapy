from celery import Celery

# Create a Celery instance with RPC result backend
app = Celery('tasks', broker='amqp://guest:guest@localhost//', backend='rpc')

# Send the task
result = app.send_task('celery_worker.tasks.run_spider')

# Check the result of the task execution
print(result.get())
