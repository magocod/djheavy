"""
...
"""

# standard library
# import json
# import binascii
# import os


# third-party
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Django
from django.conf import settings
from django.core.cache import cache

# from django.core.mail import send_mail
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string

# from django.http import JsonResponse

# local Django
from apps.mail import tasks


@api_view(["POST"])
def send_emails(request):
    """
    ...
    """

    # print("call task")
    # json_data = json.loads(request.body.decode("utf-8"))
    # print(json_data)
    if not settings.DEBUG:  # pragma: no cover
        tasks.simulate_send_emails.delay(request.data["text"])

    return Response("Emails sended using Celery", status=status.HTTP_200_OK)


@api_view(["POST"])
def sign_up_form(request):
    """
    ...
    """

    # user logic
    # ...
    if not settings.DEBUG:  # pragma: no cover
        tasks.send_email_activation.delay(
            request.data["username"], request.data["email"]
        )

    return Response(
        "We have sent you an email, "
        + "please confirm your email address to complete registration",
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
def activate_account(request, token):
    """
    ...
    """

    # print(token)
    cache_token = cache.get(token)
    # print(cache_token)
    if cache_token is None:
        return Response(
            "Activation link is invalid!", status=status.HTTP_400_BAD_REQUEST
        )

    # verify token
    # ...

    return Response(
        "Your account has been activate successfully", status=status.HTTP_200_OK
    )
