from django.shortcuts import render
from .models import Movie
# Create your views here.

def catalog(request):
    movies_list = Movie.objects.all()
    return render(request, 'movies/catalog.html', {'movies': movies_list})

def movie(request, name):
    movie = Movie.objects.filter(name=name)
    return render(request, 'movies/movie.html', {'movie': movie})