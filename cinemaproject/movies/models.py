from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', blank=False)
    description = models.TextField(max_length=500, verbose_name='Описание', blank=False)
    created_year = models.DateField(null=True, blank=True)
    rating = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Рейтинг')
    avatar = models.ImageField(upload_to='movies_images', blank=True, null=True, verbose_name='Аватар')
    box_office = models.BigIntegerField(null=True, blank=True, verbose_name='Кассовые сборы')
    budgets = models.BigIntegerField(null=True, blank=True, verbose_name='Бюджет')

    class Meta:
        db_table = 'Фильмы'
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
    
    def __str__(self):
        return self.name
