# Django
from django.core.management import call_command
from django.test import TestCase

# local Django
from apps.product.models import Product
from apps.product_type.models import ProductType


class ProductCommandTestCase(TestCase):
    """
    ...
    """

    def test_command_create_list_of_products(self):
        """
        ...
        """

        ProductType.objects.create(name="test", price=100)
        products_quantity: int = 5
        call_command("create_products", str(products_quantity))
        self.assertEqual(Product.objects.count(), products_quantity)
