import logging
from django.shortcuts import render


logger = logging.getLogger(__name__)


def index(request):
    context = {
        "title": "Home",
        "content": "Добро пожаловать",
    }
    logger.info("Index page accessed")
    return render(request, "index.html", context)


def about(request):
    context = {
        "title": "О себе",
    }
    logger.info("About page accessed")
    return render(request, "about.html", context)
