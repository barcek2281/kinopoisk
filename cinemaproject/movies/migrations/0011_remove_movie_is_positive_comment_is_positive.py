# Generated by Django 5.0.6 on 2024-07-21 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_movie_is_positive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='is_positive',
        ),
        migrations.AddField(
            model_name='comment',
            name='is_positive',
            field=models.BooleanField(blank=True, null=True, verbose_name='положительный'),
        ),
    ]
