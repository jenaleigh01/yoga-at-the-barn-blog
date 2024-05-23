from django.shortcuts import render
from django.views import generic

# Create your views here.


def about_me(request):
    """
    Renders the About page
    """
    return render(request, 'about/about_page.html')

