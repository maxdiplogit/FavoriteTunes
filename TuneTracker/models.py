from django.db import models


# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=300)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title