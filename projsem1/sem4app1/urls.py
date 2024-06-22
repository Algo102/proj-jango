from django.urls import path
from .views import flip_coin, roll_cube, random_number, perform_action
from .views import add_author, add_article, articles

urlpatterns = [
    path('fl_cn/<int:tryes>/', flip_coin, name='flip_coin'),
    path('fl_cb/<int:tryes>/', roll_cube, name='roll_cube'),
    path('fl_nr/<int:tryes>/', random_number, name='random_number'),
    path('fl_all/', perform_action, name='perform_action'),
    path('author/', add_author, name='add_author'),
    path('add_article/', add_article, name='add_article'),
    path('articles/', articles, name='articles'),
]
