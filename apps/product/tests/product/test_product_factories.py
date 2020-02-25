# Django
from django.test import TestCase

# local Django
from apps.product.db.factories import ProductFactory
from apps.product.models import Product
from apps.product_type.db.factories import ProductTypeFactory


class FactoryProductTestCase(TestCase):
    """
    ...
    """

    def test_factory_product(self):
        """
        ...
        """

        products_quantity: int = 5
        ProductFactory.create_batch(size=products_quantity)
        self.assertEqual(Product.objects.count(), products_quantity)

    def test_factory_product_poblate(self):
        """
        ...
        """

        products_quantity: int = 5
        ProductTypeFactory.create_batch(size=5)
        ProductFactory.create_batch(size=products_quantity)
        self.assertEqual(Product.objects.count(), products_quantity)

    # def test_factory_product_ramdom(self):
    #     """
    #     ...
    #     """

    #     products_quantity: int = 5
    #     ProductTypeFactory.create_batch(size=5)
    #     ProductFactory.create_batch(size=products_quantity)
    #     self.assertEqual(Product.objects.count(), products_quantity)
