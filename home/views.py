from django.shortcuts import render
from django.views import generic

# Create your views here.


def index(request):
    """
    Renders the Homepage View
    """
    return render(request, 'home/index.html')


