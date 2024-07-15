from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
	path('movie/<slug:movie_slug>', views.movie, name='movie'),
	path('', views.catalog, name="catalog"),
    path('<int:page>', views.catalog, name='catalog'),
  
]
