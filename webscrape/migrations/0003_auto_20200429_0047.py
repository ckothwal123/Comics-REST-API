# Generated by Django 3.0.5 on 2020-04-29 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webscrape', '0002_comics'),
    ]

    operations = [
        migrations.DeleteModel(
            name='heartAndBrain',
        ),
        migrations.RenameField(
            model_name='comics',
            old_name='s3_bucket_link',
            new_name='image_link',
        ),
    ]
