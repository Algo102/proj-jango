from django.shortcuts import render
import logging
from django.http import HttpResponse
import random

logger = logging.getLogger(__name__)


def home(request):
    logger.info('home page accessed')
    return HttpResponse(f"<h1>Страница случайных игр</h1>")


def coin(request):
    logger.info('Coin page accessed')
    res = random.choice(['ОРЕЛ', 'РЕШКА'])
    return HttpResponse(f'Результат подбрасывания монеты: <h1>{res}</h1>')


def random_roll(request):
    logger.info('Cube page accessed')
    res = random.randint(1, 6)
    return HttpResponse(f'Вам выпал кубик со стороной: <h1>{res}</h1>')


def random_num(request):
    logger.info('Random numbers page accessed')
    res = random.randint(0, 100)
    return HttpResponse(f'Вам выпало случайное число от 0..100: <h1>{res}</h1>')
