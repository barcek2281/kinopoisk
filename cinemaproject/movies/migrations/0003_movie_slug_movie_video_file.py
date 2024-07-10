# Generated by Django 5.0.6 on 2024-07-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_options_alter_movie_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='movie',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='movie_videos', verbose_name='Видео'),
        ),
    ]
