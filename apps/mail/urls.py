from django.urls import path

from apps.mail.views import send_emails


urlpatterns = [
    path("send_emails/", send_emails),
]
