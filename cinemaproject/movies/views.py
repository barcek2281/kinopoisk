from django.http import Http404
from django.shortcuts import render
from django.template import context
from .models import Movie
# Create your views here.

def catalog(request, query=None):
    query = request.GET.get('q', None)
    rating = request.GET.get('rating', None)
    
    movies = Movie.objects.all()
    
    if query:
        movies = movies.filter(name__icontains=query)
    if rating:
        movies = movies.filter(rating__gte=rating)
    if not movies.exists():
        raise Http404("No movies found matching the criteria.")
        
    context = {
        'movies': movies
  }
    return render(request, 'movies/catalog.html', context)

def movie(request, movie_slug):
    movie = Movie.objects.get(slug=movie_slug)
    context = {
        'movie': movie
  }
    return render(request, 'movies/movie.html', context)
