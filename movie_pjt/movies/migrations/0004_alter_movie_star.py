# Generated by Django 3.2.12 on 2022-09-30 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movie_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='star',
            field=models.CharField(default='⭐⭐⭐', max_length=20),
        ),
    ]
