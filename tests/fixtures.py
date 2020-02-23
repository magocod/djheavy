"""
...
"""

# Django
from django.test import TestCase

# local Django
from apps.product.db.factories import ProductPoblateFactory
from apps.product.db.factories import ProductTypeFactory


class ProductTestCase(TestCase):
    """
    ...
    """

    def setUp(self):
        """
        ...
        """

        self.create_products_types(5)
        self.create_products(10)

    def create_products_types(self, quantity: int):
        """
        ...
        """
        ProductTypeFactory.create_batch(size=quantity)

    def create_products(self, quantity: int):
        """
        ...
        """

        ProductPoblateFactory.create_batch(size=quantity)
