"""
...
"""

# standard library
import datetime

# third-party
import factory
from factory import fuzzy

import pytz

# local Django
from apps.product.models import Product
from apps.product_type.models import ProductType
from apps.product_type.db import factories as ptypefactories


class ProductFactory(factory.django.DjangoModelFactory):
    """
    ...
    """

    ptype = factory.SubFactory(ptypefactories.ProductTypeFactory)
    count = fuzzy.FuzzyInteger(0, 10000)
    updated = fuzzy.FuzzyDateTime(
        start_dt=datetime.datetime(2020, 1, 1, 0, 0, tzinfo=pytz.UTC),
        end_dt=datetime.datetime(2020, 3, 4, 0, 0, tzinfo=pytz.UTC),
    )

    class Meta:
        """
        ...
        """

        model = Product

    @factory.post_generation
    def set_timestamp(self, create, extracted, **kwargs):
        if not create:
            return

        # print(self.id)
        # print(self.updated.timestamp())
        # print(self.updated.timestamp())
        # self.timestamp = self.updated.timestamp()
        # self.save()
        return


class ProductPoblateFactory(ProductFactory):
    """
    ...
    """

    ptype = factory.Iterator(ProductType.objects.all())


class ProductRamdomFactory(ProductFactory):
    """
    ...
    """

    ptype = fuzzy.FuzzyInteger(1, 5)
