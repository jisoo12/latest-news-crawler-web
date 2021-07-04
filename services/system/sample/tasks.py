from celery import Celery
import time


BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'


app = Celery('tasks', broker=BROKER_URL, backend=CELERY_RESULT_BACKEND)

@app.task
def add(x, y):
  return x + y

@app.task
def practice(x, y):
  # time.sleep(5)
  text = "{0} : {1}".format(x, y)
  return text
