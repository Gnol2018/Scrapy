# tasks.py or celeryconfig.py

from celery import Celery
from celery.schedules import crontab
from celery_worker.tasks import run_spider

app = Celery('tasks', broker='amqp://guest:guest@localhost//')

app.conf.beat_schedule = {
    'run-spider-every-hour': {
        'task': 'celery_worker.tasks.run_spider',
        'schedule': crontab(minute="*"),  # Run every hour
    },
}
