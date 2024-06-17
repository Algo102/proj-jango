from django.core.management.base import BaseCommand
from sem2app1.models import Article, Author


class Command(BaseCommand):
    help = "Create article."

    def handle(self, *args, **kwargs):
        article = Article(
            title='Jack',
            text='capitan Vorobey',
            author=Author.objects.filter(pk=1).first(),
            category='Some Categories',
            )
        article.save()
        self.stdout.write(f'Статья {article.title} добавлена')
