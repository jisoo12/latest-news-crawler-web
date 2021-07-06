from celery import Celery

def make_celery(app):
  celery = Celery(
    app.import_name,
    backend=app.config['CELERY_RESULT_BACKEND'],
    broker=app.config['CELERY_BROKER_URL']
  )
  celery.conf.update(app.config)

  class ContextTask(celery.Task):
    def __call__(self, *args, **kwagrs):
      with app.app_context():
        return self.run(*args, **kwagrs)

  celery.Task = ContextTask
  return celery


from flask import Flask

flask_app = Flask(__name__)

@flask_app.route('/')
def hello():
  return 'hello celery!!!'

@flask_app.route('/task')
def test_1():
  rst = say_hello.delay('soosoo')
  print(rst)
  return 'ok'

# @flask_app.route('/status')
# def status_1():
#   rst = add_together.AsyncResult('task_id')
#   return rst

def on_raw_message(body):
  print(body)

flask_app.config.update(
  CELERY_BROKER_URL='redis://localhost:6379',
  CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(flask_app)

@celery.task()
def say_hello(name):
  return "Hello {0}".format(name)
