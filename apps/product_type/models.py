from django.db import models
from django.utils import timezone


class ProductType(models.Model):
    """
    ...
    """

    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    updated = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
