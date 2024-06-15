from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('coin/', views.coin, name='coin'),
    path('random_roll/', views.random_roll, name='random_roll'),
    path('random_num/', views.random_num, name='random_num'),
]