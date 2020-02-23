from __future__ import absolute_import, unicode_literals
from celery import shared_task

# from time import sleep

from apps.mail.models import Mail

# from djheavy.celery import app


@shared_task
def simulate_send_emails(n: int):
    print(n)
    Mail.objects.create(name="send email")
    return "Emails sended"


@shared_task
def add(x, y):
    return x + y
