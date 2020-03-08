"""
...
"""

# standard library
import datetime

# third-party
import factory
import pytz
from factory import fuzzy

# local Django
from apps.product_type.models import ProductType


class ProductTypeFactory(factory.django.DjangoModelFactory):
    """
    ...
    """

    name = factory.Sequence(lambda n: f"product n: {n}")
    price = fuzzy.FuzzyDecimal(0.1, 100000.5)
    updated = fuzzy.FuzzyDateTime(
        start_dt=datetime.datetime(2020, 1, 1, 0, 0, tzinfo=pytz.UTC),
        end_dt=datetime.datetime(2020, 4, 4, 0, 0, tzinfo=pytz.UTC),
    )

    class Meta:
        """
        ...
        """

        model = ProductType
