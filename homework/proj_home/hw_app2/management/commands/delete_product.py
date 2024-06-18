from django.core.management.base import BaseCommand
from hw_app2.models import Product


class Command(BaseCommand):
    help = "Create client."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get("pk")
        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            product.delete()
            self.stdout.write(self.style.WARNING(f"Product {product.title} is deleted"))
