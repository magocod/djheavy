"""
...
"""

# Django
from django.core.management.base import BaseCommand

# local Django
from apps.product.db.factories import ProductPoblateFactory


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
        print(f"generating... :{quantity} (products)")
        ProductPoblateFactory.create_batch(size=quantity)
        print("...completed")
