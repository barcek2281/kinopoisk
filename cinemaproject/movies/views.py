from django.shortcuts import render
from .models import Movie
# Create your views here.

def catalog(request):

    movies_list = Movie.objects.all()
    return render(request, 'movies/catalog.html', {'movies': movies_list})
