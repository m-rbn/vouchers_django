from django import forms

class vchr_form(forms.Form):
    code_input = forms.IntegerField(label = 'CODE')
