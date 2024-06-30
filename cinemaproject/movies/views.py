from django.shortcuts import render
from .models import Movie
# Create your views here.

def catalog(request):
    #movies_list = Movie.get
    return render(request, 'catalog.html')