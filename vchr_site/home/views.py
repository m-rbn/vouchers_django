from django.shortcuts import render

# Link to template
def home_navigate(request):
    return render(request, 'home/home_navigate.html', {})
