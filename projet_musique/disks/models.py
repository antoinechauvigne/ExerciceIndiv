from django.db import models

# Create your models here.


class Track(models.Model):
    name = models.CharField(max_length=200)
    composer = models.CharField(max_length=200)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField()
    unitPrice = models.DecimalField(max_digits=4, decimal_places=2)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)


    class Meta:  # qui est optionnelle
        verbose_name = "track"
        ordering = ['name']

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)


    class Meta:  # qui est optionnelle
        verbose_name = "album"
        ordering = ['title']

    def __str__(self):
        return self.title

class Artist(models.Model):
    name = models.CharField(max_length=200)

    class Meta:  # qui est optionnelle
        verbose_name = "artist"
        ordering = ['name']

    def __str__(self):
        return self.name