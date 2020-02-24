"""
...
"""

import json

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from apps.mail.tasks import simulate_send_emails


@csrf_exempt
def send_emails(request):
    """
    ...
    """

    # print("call task")
    json_data = json.loads(request.body.decode("utf-8"))
    simulate_send_emails.delay(json_data["text"])
    return JsonResponse({"email": "Emails sended using Celery"})
