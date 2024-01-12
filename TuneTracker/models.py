from django.db import models


# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=300, unique=True)
    color = models.CharField(max_length=7, default='#5f9ea0')
    
    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=300)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('title', 'artist')
    
    def __str__(self):
        return f"{self.title} by {self.artist.name}"