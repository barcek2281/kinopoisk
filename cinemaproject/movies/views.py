from django.shortcuts import render
from django.template import context
from .models import Movie
# Create your views here.

def catalog(request):
    movies_list = Movie.objects.all()
    return render(request, 'movies/catalog.html', {'movies': movies_list})

def movie(request, movie_slug):
    movie = Movie.objects.get(slug=movie_slug)
    context = {
        'movie': movie
	}
    return render(request, 'movies/movie.html', context)

