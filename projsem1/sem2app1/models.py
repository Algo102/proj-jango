from django.db import models


class CoinFlip(models.Model):
    RESULT_CHOICES = [
        ('heads', 'Орёл'),
        ('tails', 'Решка'),
    ]

    result = models.CharField(max_length=5, choices=RESULT_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_last_flips(n: int):
        flips = CoinFlip.objects.order_by('-timestamp')[:n]
        stats = {'heads': 0, 'tails': 0}
        for flip in flips:
            if flip.result == 'heads':
                stats['heads'] += 1
            else:
                stats['tails'] += 1
        return stats

    def __str__(self):
        return f"{self.result} at {self.timestamp}"

# Чтоб все работало, нужно чтоб БД была не пустая. Можно сделать ч.з. терминал
# python manage.py shell - входим в консоль Django shell
# from sem2app1.models import CoinFlip
# from django.utils import timezone
#
# CoinFlip.objects.create(result='heads', timestamp=timezone.now())
# CoinFlip.objects.create(result='tails', timestamp=timezone.now())
# CoinFlip.objects.create(result='heads', timestamp=timezone.now())


class Author(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField()

    def full_name(self):
        return f"{self.name} {self.lastname}"


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)

