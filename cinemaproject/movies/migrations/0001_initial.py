# Generated by Django 5.0.6 on 2024-06-28 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('created_year', models.DateField()),
                ('rating', models.IntegerField()),
                ('avatar', models.ImageField(upload_to='')),
                ('box_office', models.BigIntegerField()),
                ('budgets', models.BigIntegerField()),
            ],
        ),
    ]
