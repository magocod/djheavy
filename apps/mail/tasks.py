from __future__ import absolute_import, unicode_literals

# from time import sleep
import binascii
import os

from celery import shared_task
from django.conf import settings

# Django
from django.core.cache import cache
from django.core.mail import send_mail
from django.template.loader import render_to_string

# local Django
from apps.mail.models import Mail
from apps.utils.basetaskcelery import VerifyTaskBase
from djheavy.celery import app


@app.task(base=VerifyTaskBase)
def example_add(x: int, y: int):
    """
    ...
    """

    return x + y


@shared_task
def simulate_send_emails(text: str):
    """
    ...
    """

    Mail.objects.create(name=text)
    # print("task db", Mail.objects.count())

    if settings.ACTIVE_EMAIL:  # pragma: no cover
        subject = "Thank you for registering to our site"
        message = " it  means a world to us "
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [text]
        send_mail(subject, message, email_from, recipient_list)

    dict_task = {
        "sended_to": text,
    }
    return dict_task


@shared_task
def send_email_activation(username: str, email: str, domain: str):
    """
    ...
    """

    token: str = binascii.hexlify(os.urandom(20)).decode()

    if settings.ACTIVE_EMAIL:  # pragma: no cover
        subject = "Thank you for registering to our site"
        message = render_to_string(
            "activate_account.html",
            {"username": username, "domain": domain, "token": token,},
        )

        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)

    cache.set(token, f"{username}_{email}_{token}", 60)

    return token
