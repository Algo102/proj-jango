from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# default - обязательное поле. Тут в дате не указали, но при миграции попросит изменить или принять текущее
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(default='', blank=True)  # по умолчанию пусто и поле НЕ обязательное
    price = models.DecimalField(default=999999.99, max_digits=8, decimal_places=2)  # DecimalField для точности, а не Float
    quantity = models.PositiveSmallIntegerField(default=0)  # Положительное, пару байт, целое
    date_added = models.DateTimeField(auto_now_add=True)  # Автоматическая подстановка времени сервера
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name
