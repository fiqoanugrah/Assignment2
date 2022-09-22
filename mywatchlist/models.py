from django.db import models

# Create your models here.
class WatchList(models.Model):
    watched = models.BooleanField(max_length=50)
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.TextField()
    review = models.TextField()