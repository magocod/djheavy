from django.db import models


class Mail(models.Model):
    """
    ...
    """

    name = models.CharField(max_length=200)
    sent = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
