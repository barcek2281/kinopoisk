from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    created_year = models.DateField()
    rating = models.IntegerField() 
    avatar = models.ImageField()
    box_office = models.BigIntegerField()
    budgets = models.BigIntegerField()


