# Generated by Django 3.0.5 on 2020-06-10 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webscrape', '0006_titles_comic_catalog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='titles',
            name='comic_catalog',
        ),
    ]
