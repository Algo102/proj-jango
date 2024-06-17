from django.urls import path
from . import views

urlpatterns = [
    path('', views.index2, name='index2'),
    path('coin1/', views.coin_v1, name='coin_flip1'),
    # path('coin2/', views.coin_v2, name='coin_flip2'),
]
