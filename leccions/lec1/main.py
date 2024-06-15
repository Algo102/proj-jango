# python -m venv .venv
# .venv\Scripts\activate.ps1 для PWSH, если нет то, без .ps1
# deactivate - дективировать виртуальну среду
# pip list - посмотреть установленные зависимости в консоль
# pip freeze - посмотреть установленные зависимости в др. поток вывода
# pip freeze > requirements.txt - сохранить установленные зависимости

# pip install django

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
#
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
