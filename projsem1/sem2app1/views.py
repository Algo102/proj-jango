from django.shortcuts import render
from django.http import HttpResponse
from sem2app1.models import CoinFlip
import random
import logging

logger = logging.getLogger(__name__)


def index2(request):
    return HttpResponse("Семинар2, программа1")


def coin_v1(request):
    flip = CoinFlip.get_last_flips(3)  # получаем 3 последних значения из БД
    return render(request, 'coin_flip.html', {'flip': flip})


# def coin_v1(request):
#     flips = CoinFlip.objects.all()
#     return HttpResponse(f"flips: {flips}")

# def coin_v1(request):
#     result = random.choice(['Heads', 'Tails'])
#     flips = CoinFlip.objects.create(result=result)
#     return HttpResponse(f"flips: {flips}")


# def coin_v2(request):
#     flips = CoinFlip.objects.all()
#     return render(request, "coin_flip_template.html", {'flips': flips})


# def coin_flip_view(request):
#     flips = CoinFlip.objects.all()
#     return render(request, "coin_flip_template.html", {'flips': flips})
