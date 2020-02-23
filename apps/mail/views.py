"""
...
"""

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from apps.mail.tasks import simulate_send_emails


@csrf_exempt
def send_emails(request):
    """
    ...
    """

    print("call task")
    simulate_send_emails.delay(1)
    return JsonResponse({"email": "Emails sended using Celery"})
