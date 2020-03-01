from django.urls import path

from apps.mail import views


urlpatterns = [
    path("send_emails/", views.send_emails),
    path("email/sign_up/", views.sign_up_form),
    path("activate/<slug:token>/", views.activate_account),
]
