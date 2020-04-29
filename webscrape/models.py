from django.db import models


#Model for the table to hold all comics and links
class Comics(models.Model):
    comic_title = models.CharField(max_length=100)
    comic_type=models.CharField(max_length=100)
    image_link = models.TextField()