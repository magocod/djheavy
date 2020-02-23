from django.db import models
from django.utils import timezone

from apps.product_type.models import ProductType


class Product(models.Model):
    """
    ...
    """

    ptype = models.ForeignKey(ProductType, on_delete=models.PROTECT)
    count = models.DecimalField(max_digits=10, decimal_places=2)
    updated = models.DateTimeField(default=timezone.now)
    timestamp = models.IntegerField(default=0)
