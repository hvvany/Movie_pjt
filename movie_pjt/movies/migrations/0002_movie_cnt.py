# Generated by Django 3.2.12 on 2022-09-30 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cnt',
            field=models.IntegerField(default=0),
        ),
    ]