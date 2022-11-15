from __future__ import absolute_import, unicode_literals
from celery.schedules import crontab
from core.celery import app as celery_app
from api.models import Transactions
from users.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.hashers import make_password
from django.template.loader import render_to_string


@celery_app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute=0, hour=0), auto_add.s())
    

@celery_app.task
def auto_add():
    for user in User.objects.all().values('id', 'email', 'salary', 'username'):
        try:
            message = render_to_string('email.html', {
                        'user': user['username'],
                        'salary': user['salary'],
                    }) 
            mail = EmailMessage('your stat acc!', message, to=[user['email']])
            mail.send()
        except Exception as error:
            print(error)
    

