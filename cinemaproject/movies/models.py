from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50, verbose_name='Жанр', blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    
    class Meta:
        db_table = 'Жанры'
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ("id",)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', blank=False)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(max_length=500, verbose_name='Описание', blank=False)
    created_year = models.DateField(null=True, blank=True)
    rating = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Рейтинг')
    avatar = models.ImageField(upload_to='movies_images', blank=True, null=True, verbose_name='Аватар')
    box_office = models.BigIntegerField(null=True, blank=True, verbose_name='Кассовые сборы')
    budgets = models.BigIntegerField(null=True, blank=True, verbose_name='Бюджет')
    video_file = models.FileField(upload_to='movie_videos', blank=True, null=True, verbose_name='Видео')
    genre = models.ForeignKey(to=Genre, on_delete=models.CASCADE, verbose_name='Жанр', null=True)

    class Meta:
        db_table = 'Фильмы'
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ('id',) 
    
    def __str__(self):
        return self.name
    
