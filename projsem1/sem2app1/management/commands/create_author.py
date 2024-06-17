from django.core.management.base import BaseCommand
from sem2app1.models import Author


class Command(BaseCommand):
    help = "Create author."

    def handle(self, *args, **kwargs):
        author = Author(
            name='Shamil',
            lastname='Mentarov',
            email='asdf@ssdf.ru',
            bio='Text text',
            birthday='1999-12-31',
            )
        author.save()
        self.stdout.write(f'Автор {author.full_name()} добавлена')
