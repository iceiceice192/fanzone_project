
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings/', views.user_settings, name='settings'),
    path('favorites/', views.favorites, name='favorites'),
    path('clear/', views.clear_cookies, name='clear_cookies'),
]
