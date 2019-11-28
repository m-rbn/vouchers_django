'''This module contains the form class to be rendered alongside the html template'''
from django import forms

class VchrForm(forms.Form):
    '''The form contains only one character field  data'''

    code_input = forms.CharField(label='CODE', max_length=5)
