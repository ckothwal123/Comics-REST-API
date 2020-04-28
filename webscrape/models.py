from django.db import models

# Create your models here.
class HeartAndBrain(models.Model):
    heading = models.TextField()
    src_link = models.TextField()
    

#Model for the table to hold all comics and links
class Comics(models.Model):
    comic_title = models.CharField(max_length=100)
    comic_type=models.CharField(max_length=100)
    s3_bucket_link = models.TextField()