"""
...
"""

# standard library
# import json

# third-party
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from django.http import JsonResponse
from apps.mail.tasks import simulate_send_emails


@api_view(['POST'])
def send_emails(request):
    """
    ...
    """

    # print("call task")
    # json_data = json.loads(request.body.decode("utf-8"))
    # print(json_data)
    simulate_send_emails.delay(request.data["text"])
    return Response("Emails sended using Celery")
