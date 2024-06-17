# https://github.com/github/gitignore/blob/main/Python.gitignore
# python -m venv .venv - СОЗДАНИЕ СРЕДЫ
# .venv\Scripts\activate.ps1 для PWSH, если нет то, без .ps1
# deactivate - дективировать виртуальну среду
# pip list - посмотреть установленные зависимости в консоль
# pip freeze - посмотреть установленные зависимости в др. поток вывода
# pip freeze > requirements.txt - сохранить установленные зависимости

# pip install django

# СОЗДАЕМ ПРОЕКТ
# django-admin startproject myproject1
# появилась папка в которой есть
# asgi - для взаимодействия с сихронным сервером
# wsgi - для взаимодействия с асихронным сервером
# cd .\myproject1\

# python manage.py runserver
# или любой порт или ip, например 0.0.0.0 для всех в локальной сети
# python manage.py runserver 8080
# python manage.py runserver 0.0.0.0:8080

# ipconfig - посмотреть свой ip
# В settings можем прописать свой ip, чтоб локальные хосты тоже могли смотреть
# ALLOWED_HOSTS = [
#     '192.168.0.53',
#     '127.0.0.1',
# ]

# так зайдет любой ip адрес
# ALLOWED_HOSTS = ['*/*']

# Создание приложения
# python manage.py startapp myapp

# Дописываем приложение в проект
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'myapp',
# ]

# в myapp добавляем во views нужные изменения
# Попроще без логера
# from django.http import HttpResponse  # Класс для ответа от сервера к клиенту
#
#
# def index(request):
#     return HttpResponse("Hello, world!")
#
#
# def about(request):
#     return HttpResponse("About us")


# По сложнее и с логером
# import logging
# from django.http import HttpResponse  # Класс для ответа от сервера к клиенту
#
# logger = logging.getLogger(__name__)
#
#
# def index(request):
#     logger.info('Index page accessed')
#     return HttpResponse("Hello, world!")
#
#
# def about(request):
#     try:
#         # some code that might raise an exception
#         result = 1 / 0
#     except Exception as e:
#         logger.exception(f'Error in about page: {e}')
#         return HttpResponse("Oops, something went wrong.")
#     else:
#         logger.debug('About page accessed')
#         return HttpResponse("This is the about page.")


# Настройка путей:
# Открываем urls.py в корневой директории проекта, если несколько программ
# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('sem1app.urls')),
#     path('', include('sem1app2.urls')),
# ]

# соединяем маршруты и представления
# в myapp создаем файл urls.py
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('about/', views.about, name='about'),
#     path('coin/', views.coin, name='coin'),
#     path('random_roll/', views.random_roll, name='random_roll'),
#     path('random_num/', views.random_num, name='random_num'),
# ]

# Можно запускать сервер
# python manage.py runserver
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/about/


# Логирование, настраиваем - settings
# дописываем LOGGING = {}
# в проекте создаем папку log

# LOGGING = {
#     'version': 1,  # наша версия логирования
#     'disable_existing_loggers': False,  # не исключаем другое логирование
#     'formatters': {
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#         'verbose': {
#             'format': '{levelname} {asctime} {module} {process} {thread} {message}',
#             'style': '{',
#         },
#     },
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose'
#         },
#         'file': {
#             'class': 'logging.FileHandler',
#             'filename': './log/django.log',
#             'formatter': 'verbose'
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'file'],
#             'level': 'INFO',
#         },
#         'myapp': {
#             'handlers': ['console', 'file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }

# Таким образом можно сделать логирование нескольких программ в одном проекте
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#         'verbose': {
#             'format': '{levelname} {asctime} {module} {process} {thread} {message}',
#             'style': '{',
#         },
#     },
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose'
#         },
#         'file1': {
#             'class': 'logging.FileHandler',
#             'filename': './log/django1.log',
#             'formatter': 'verbose'
#         },
#         'file2': {
#             'class': 'logging.FileHandler',
#             'filename': './log/django2.log',
#             'formatter': 'verbose'
#         },
#     },
#     'loggers': {
#         'django1': {
#             'handlers': ['console', 'file1'],
#             'level': 'INFO',
#         },
#         'django2': {
#             'handlers': ['console', 'file2'],
#             'level': 'INFO',
#         },
#         'sem1app': {
#             'handlers': ['console', 'file1'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'sem1app2': {
#             'handlers': ['console', 'file2'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }

#########################################################################
# СОЗДАНИЕ МОДЕЛИ
# внутри приложения переходим в models.py
# from django.db import models
#
#
# class User(models.Model):  # id добавляется автоматически
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     password = models.CharField(max_length=100)
#     age = models.IntegerField()
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     description = models.TextField()
#     image = models.ImageField(upload_to='products/')
#
#
# class Order(models.Model):
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     total_price = models.DecimalField(max_digits=8, decimal_places=2)

# Описание полей модели
# Django предоставляет множество типов полей
# ● CharField - поле для хранения строковых данных
# ● EmailField - поле для хранения электронной почты
# ● TextField - поле для хранения текстовых данных большой длины
# ● IntegerField - поле для хранения целочисленных данных
# ● DecimalField - поле для хранения десятичных чисел
# ● FloatField - поле для хранения десятичных чисел, проблемы с точностью
# ● BooleanField - поле для хранения логических значений (True/False)
# ● DateTimeField - поле для хранения даты и времени
# ● DateField - поле для хранения даты
# ● TimeField - поле для хранения времени
# ● ForeignKey - поле для связи с другой моделью. Один ко многим
# ● ManyToManyField - поле для связи с другой моделью в отношении "многие-ко-многим"
# ● ImageField - для работы с изображнием === pip install pillow
# https://docs.djangoproject.com/en/4.2/ref/models/fields/#model-field-types


# МИГРАЦИИ
# если не указывать приложение, то зоздадутся миграции для всех приложений
# python manage.py makemigrations lecapp2

# применяем все накопленные миграции(появятся все таблицы)
# python manage.py migrate


# СОБСТВЕННЫЕ КОМАНДЫ
# в приложении создаем пакет management
# внутри него создаем пакет commands

# внутри создаем файлы с командами my_command.py
# в нем прописываем свою команду
# from django.core.management.base import BaseCommand
#
#
# class Command(BaseCommand):
#     help = "Print 'Hello world!' to output."
#
#     def handle(self, *args, **kwargs):
#         self.stdout.write('Hello world!')

# затем в консоле можно запросить справку
# python manage.py my_command -h

# для вывода Hello world!
# python manage.py my_command


# создаем команду добавления пользователя create_user.py
# from django.core.management.base import BaseCommand
# from lecapp2.models import User
#
#
# class Command(BaseCommand):
#     help = "Create user."
#
#     def handle(self, *args, **kwargs):
#         user = User(name='John', email='john@example.com', password='secret', age=25)
#         ...
#         user.save()
#         self.stdout.write(f'{user}')
#
# python manage.py create_user

# для лучшего представления при выводе в класс User в файле models добавляем
# def __str__(self):
#     return f'Username: {self.name}, email: {self.email}, age: {self.age}'


# Получение объектов модели из базы данных, read. "all()" и "get()" и "filter()"
# создаем файл get_all_users.py  - команда для вывода всех юзеров
# from django.core.management.base import BaseCommand
# from lecapp2.models import User
#
#
# class Command(BaseCommand):
#     help = "Get all users."
#
#     def handle(self, *args, **kwargs):
#         users = User.objects.all()
#         self.stdout.write(f'{users}')

# создаем файл get_user.py - команда для вывода одного юзера
# from django.core.management.base import BaseCommand
# from lecapp2.models import User
#
#
# class Command(BaseCommand):
#     help = "Get user by id."
#
#     def add_arguments(self, parser):
#         parser.add_argument('id', type=int, help='User ID')
#
#     def handle(self, *args, **kwargs):
#         id = kwargs['id']
#         user = User.objects.get(id=id)
#         self.stdout.write(f'{user}')

# python manage.py get_user 2

# Для получения None, а не ошибок при поиске несуществующего пользователя
# нужно использовать pk(первичный ключ) и filter вместо get
# from django.core.management.base import BaseCommand
# from lecapp2.models import User
#
#
# class Command(BaseCommand):
#     help = "Get user by id."
#
#     def add_arguments(self, parser):
#         parser.add_argument('pk', type=int, help='User ID')
#
#     def handle(self, *args, **kwargs):
#         pk = kwargs['pk']
#         user = User.objects.filter(pk=pk).first()
#         self.stdout.write(f'{user}')

# метод filter()
# Model.objects.filter(param__filter=value)
# ● exact - точное совпадение значения поля
# ● iexact - точное совпадение значения поля без учета регистра
# ● contains - значение поля содержит заданный подстроку
# ● icontains - значение поля содержит заданный подстроку без учета регистра
# ● in - значение поля находится в заданном списке значений
# ● gt - значение поля больше заданного значения
# ● gte - значение поля больше или равно заданному значению
# ● lt - значение поля меньше заданного значения
# ● lte - значение поля меньше или равно заданному значению
# ● startswith - значение поля начинается с заданной подстроки
# ● istartswith - значение поля начинается с заданной подстроки без учета регистра
# ● endswith - значение поля заканчивается на заданную подстроку
# ● iendswith - значение поля заканчивается на заданную подстроку без учета регистра
# ● range - значение поля находится в заданном диапазоне значений
# ● date - значение поля является датой, соответствующей заданной дате
# ● year - значение поля является годом, соответствующим заданному году


# создаем файл get_user_age.py - команда для вывода юзеров с фильтрацией по году
# from django.core.management.base import BaseCommand
# from lecapp2.models import User
#
#
# class Command(BaseCommand):
#     help = "Get user with age greater <age>."
#
#     def add_arguments(self, parser):
#         parser.add_argument('age', type=int, help='User age')
#
#     def handle(self, *args, **kwargs):
#         age = kwargs['age']
#         user = User.objects.filter(age__gt=age)
#         self.stdout.write(f'{user}')


# update_user.py Изменение объектов модели, update. get() или filter() в сочетании с save()
# from django.core.management.base import BaseCommand
# from lecapp2.models import User
#
#
# class Command(BaseCommand):
#     help = "Update user name by id."
#
#     def add_arguments(self, parser):
#         parser.add_argument('pk', type=int, help='User ID')
#         parser.add_argument('name', type=str, help='User name')
#
#     def handle(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         name = kwargs.get('name')
#         user = User.objects.filter(pk=pk).first()
#         user.name = name
#         user.save()
#         self.stdout.write(f'{user}')
#
# python manage.py update_user 2 Max


# Удаление объектов модели, delete
# from django.core.management.base import BaseCommand
# from lecapp2.models import User
#
#
# class Command(BaseCommand):
#     help = "Delete user by id."
#
#     def add_arguments(self, parser):
#         parser.add_argument('pk', type=int, help='User ID')
#
#     def handle(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         user = User.objects.filter(pk=pk).first()
#         if user is not None:
#             user.delete()
#         self.stdout.write(f'{user}')


