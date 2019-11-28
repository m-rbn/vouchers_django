'''This module contains the function to render the html for home page'''
from django.shortcuts import render

def home_navigate(request):
    '''This function returns a render of the html template'''
    return render(request, 'home/home_navigate.html', {})
