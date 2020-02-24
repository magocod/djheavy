# Django
from django.core.management import call_command
from django.test import TestCase

# local Django
from apps.product_type.models import ProductType


class ProductTypeCommandTestCase(TestCase):
    """
    ...
    """

    def setUp(self):
        """
        ...
        """

        pass

    def test_command_create_list_of_product_types(self):
        """
        ...
        """

        types_quantity: int = 5
        call_command("create_ptypes", str(types_quantity))
        self.assertEqual(ProductType.objects.count(), types_quantity)

    def test_command_create_list_of_product_types_retrieving_sequence(self):
        """
        ...
        """

        types_quantity: int = 5
        call_command("create_ptypes", str(types_quantity))
        call_command("create_ptypes", str(types_quantity))
        self.assertEqual(ProductType.objects.count(), types_quantity * 2)
