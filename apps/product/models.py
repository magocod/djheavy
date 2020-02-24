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


class ReportProduct(models.Model):
    """
    ...
    """

    TYPES = (("D", "DAY"), ("M", "MONTH"), ("Y", "YEAR"))
    rformat = models.CharField(max_length=1, choices=TYPES)
    total = models.TextField(default="{}")
    summary = models.TextField(default="{}")
    meta = models.TextField(default="{}")
    updated = models.DateTimeField(default=timezone.now)
    timestamp = models.DateTimeField(auto_now_add=True)
