from django.http import Http404
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.template import context
from .models import Movie, Genre, Comment
from .forms import CommentForm
# Create your views here.

def catalog(request, page=1):
    query = request.GET.get('q', None)
    rating = request.GET.get('rating', None)
    selected_genres = request.GET.getlist('genres', None)
    
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    

    if query:
        movies = movies.filter(name__icontains=query)
    if rating:
        movies = movies.filter(rating__gte=rating)
    if selected_genres:
        movies = movies.filter(genre__id__in=selected_genres).distinct()
        
    # if not movies.exists():
    #     raise Http404("No movies found matching the criteria.")
    
    paginator = Paginator(movies, 4)
    current_page = paginator.page(page)
        
    context = {
        'movies': current_page,
        'genres': genres
  }
    return render(request, 'movies/catalog.html', context)


def movie(request, movie_slug):
    movie = Movie.objects.get(slug=movie_slug)
    comments = Comment.objects.filter(movie=movie)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
            #return redirect(f'{movie_slug}')
    else:
        form = CommentForm()

    context = {
        'movie': movie,
        'comments': comments,
        'form': form,
  }
    return render(request, 'movies/movie.html', context)
