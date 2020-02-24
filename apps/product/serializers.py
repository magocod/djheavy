"""
...
"""

# third-party
from rest_framework import serializers

# Django
from apps.product.models import ReportProduct


class ReportProductSerializer(serializers.ModelSerializer):
    """
    ...
    """

    class Meta:
        model = ReportProduct
        fields = ("id", "rformat", "total", "summary", "meta", "updated", "timestamp")
