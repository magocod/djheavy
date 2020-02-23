# Django
from django.test import TestCase

# local Django
from apps.product_type.db import factories
from apps.product_type.models import ProductType


class FactoryProductTypeTestCase(TestCase):
    """
    ...
    """

    def setUp(self):
        """
        ...
        """

        pass

    def test_factory_product_type(self):
        """
        ...
        """

        types_quantity: int = 5
        factories.ProductTypeFactory.create_batch(size=types_quantity)
        self.assertEqual(ProductType.objects.count(), types_quantity)
