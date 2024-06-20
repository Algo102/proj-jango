from django.core.management.base import BaseCommand
from hw_app2.models import Product
import random


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):

        for i in range(1, 5):
            product = Product(
                title=f"product{i}",
                description=f"description{i}",
                price=i * (random.randint(2, 3)),
                quantity=random.randint(15, 40),
            )
            product.save()
        self.stdout.write(self.style.SUCCESS("Some fake products are registered"))
