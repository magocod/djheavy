from __future__ import absolute_import, unicode_literals
from celery import shared_task

# from time import sleep

# Django
# from django.core.mail import send_mail
from django.conf import settings

from apps.mail.models import Mail

# from djheavy.celery import app


@shared_task
def simulate_send_emails(text: str):
    """
    ...
    """

    Mail.objects.create(name=text)

    if settings.DEBUG: # pragma: no cover
        pass
        # subject = 'Thank you for registering to our site'
        # message = ' it  means a world to us '
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = ['receiver@gmail.com']
        # send_mail(
        #     subject,
        #     message,
        #     email_from,
        #     recipient_list
        # )

    return "Emails sended"


@shared_task
def add(x: int, y: int):
    """
    ...
    """

    return x + y
