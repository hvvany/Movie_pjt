# Generated by Django 3.2.12 on 2022-09-30 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_movie_star_again'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='star_again',
            new_name='star',
        ),
    ]
