"""
...
"""

# Django
from django.core.management.base import BaseCommand

# local Django
from apps.product_type.db.factories import ProductTypeFactory
from apps.product_type.models import ProductType


class Command(BaseCommand):
    """
    ...
    """

    def add_arguments(self, parser):
        parser.add_argument("quantity", type=int)

    def handle(self, *args, **options):
        """
        ...
        """
        quantity: int = options["quantity"]
        print(f"generating... :{quantity} (product types)")

        if ProductType.objects.first() is not None:
            product_id: id = ProductType.objects.latest("created").id
            print("sequence", product_id)
            ProductTypeFactory.reset_sequence(product_id + 1)
        ProductTypeFactory.create_batch(size=quantity)
        print("...completed")
