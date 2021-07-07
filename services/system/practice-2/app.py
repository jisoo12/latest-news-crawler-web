import os
from flask import Flask, request, render_template, session
from flask_mail import Mail, Message
from celery import Celery

app = Flask(__name__)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'flask@example.com'

# Celery configuration
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'


# Initialize extentions
mail = Mail(app)

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task
def send_async_email(email_data):
  """Background task to send an email with Flask-Mail."""
  msg = Message(email_data['subject'],
                sender=app.config['MAIL_DEFAULT_SENDER'],
                recipients=[email_data['to']])
  msg.body = email_data['body']
  with app.app_context():
    mail.send(msg)


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    return render_template('index.html', email=session.get('email', ''))
  email = request.form['email']
  session['email'] = email

  # send the email
  email_data = {
    'subject': 'Hello from Flask',
    'to': email,
    'body': 'This is a test email sent from a background Celery task.'
  }
  if request.form['submit'] == 'Send':
    # send right away
    