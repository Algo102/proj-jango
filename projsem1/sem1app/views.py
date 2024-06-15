from django.shortcuts import render
from django.http import HttpResponse  # Класс для ответа от сервера к клиенту


def index(request):
    return HttpResponse("Hello, world!")


def about(request):
    return HttpResponse("About us")
