from django.contrib import admin
from .models import Movie, Genre
# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ('name',)}

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ('name',)}