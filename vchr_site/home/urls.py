from django.urls import path

from . import views

# define urlpatterns
urlpatterns = [
    path('', views.home_navigate, name= 'home')
]
