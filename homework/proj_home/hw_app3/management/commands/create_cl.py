from django.core.management.base import BaseCommand
from hw_app3.models import Client
from faker import Faker

fake = Faker("ru_RU")


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(
            name=f'{fake.last_name_male()}',
            email=f'{fake.ascii_free_email()}',
            phone=f'{fake.phone_number()}',
            address=f'{fake.address()}',
        )
        client.save()
        self.stdout.write(self.style.SUCCESS(f"Client:'{client}' is registered"))
