from django.db import models

class Vodspec(models.Model):
    title = models.CharField(max_length=25)
    genre = models.CharField(max_length=50)
    imdb_rate = models.IntegerField()
    cast = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.cast[:20]+"..."