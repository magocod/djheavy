"""
...
"""

# Django
from django.test import TestCase

# third-party
from rest_framework.test import APIClient

# local Django
from apps.product.db.factories import ProductFactory
from apps.product.models import ReportProduct
from apps.product_type.db.factories import ProductTypeFactory


class HttpClientTestCase(TestCase):
    """
    ...
    """

    def setUp(self):
        """
        ...
        """

        self.set_http_clients()

    def set_http_clients(self):
        """
        ...
        """
        self.public_client = APIClient()


class InstanceAppTestCase(HttpClientTestCase):
    """
    ...
    """

    def setUp(self):
        """
        ...
        """

        self.set_http_clients()
        self.create_products_types(5)
        self.create_products(10)
        self.create_example_reports_products()

    def create_products_types(self, quantity: int):
        """
        ...
        """
        ProductTypeFactory.create_batch(size=quantity)

    def create_products(self, quantity: int):
        """
        ...
        """

        ProductFactory.create_batch(size=quantity)

    def create_example_reports_products(self):
        """
        ...
        """

        ReportProduct.objects.create(rformat="D",)
