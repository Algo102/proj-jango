from django.shortcuts import render, redirect
from .forms import RandomForm, AuthorForm, ArticleForm
import random

from .models import Author, Article


def flip_coin(request, tryes: int):
    flips_list = [random.choice(["Орёл", "Решка"]) for _ in range(tryes)]
    context = {"title": "Flip coin", "content": flips_list}
    return render(request, "sem4app1/coin.html", context)


def roll_cube(request, tryes: int):
    cubes_list = [random.randint(1, 6) for _ in range(tryes)]
    context = {"title": "Cube game", "content": cubes_list}
    return render(request, "sem4app1/coin.html", context)


def random_number(request, tryes: int):
    cubes_list = [random.randint(1, 100) for _ in range(tryes)]
    context = {"title": "Random numbers", "content": cubes_list}
    return render(request, "sem4app1/coin.html", context)


def perform_action(request):
    if request.method == "POST":
        form = RandomForm(request.POST)
        if form.is_valid():
            result = form.cleaned_data["event_type"]
            attempts = form.cleaned_data["attempts"]
            if result == 'coin':
                return flip_coin(request, attempts)
            elif result == 'dice':
                return roll_cube(request, attempts)
            elif result == 'number':
                return random_number(request, attempts)
    else:
        form = RandomForm()
    return render(request, "sem4app1/games.html", {'form': form})


def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            Author.objects.create(
                name=form_data['name'],
                last_name=form_data['last_name'],
                email=form_data['email'],
                bio=form_data['bio'],
                birthday=form_data['birthday'],
            )
    else:
        form = AuthorForm()
    authors = Author.objects.all()
    context = {'authors': authors, 'form': form}
    return render(request, 'sem4app1/authors.html', context)


def articles(request, id_author: int=None):
    if id_author:
        author = Author.objects.filter(id=id_author).first()
        arts = Article.objects.filter(author=author)
        title = f"Статьи автора: {author.full_name()}"
    else:
        arts = Article.objects.all()
        title = "Все статьи"
    context = {
        "title": title,
        "artcles_list": arts,
    }
    return render(request, "sem4app1/articles.html", context)


def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            Article.objects.create(
                title=form_data['title'],
                text=form_data['text'],
                author=form_data['author'],
                category=form_data['category'],
                is_published=form_data['is_published'],
            )
            return redirect('articles')
    else:
        form = ArticleForm()
    context = {'title': 'Добавить статью', 'form': form}
    return render(request, 'sem4app1/add_article.html', context)

