'''This module contains the path string for url'''
from django.urls import path
from . import views

# define urlpatterns
urlpatterns = [
    path('', views.home_navigate, name='home')
]
