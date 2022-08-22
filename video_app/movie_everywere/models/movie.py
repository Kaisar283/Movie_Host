from django.db import models
from movie_everywere.models import Directors, Genres


class Movie(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    discription = models.TextField(max_length=500, blank=False)
    director = models.ForeignKey(Directors, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genres, blank=False)
    release_date = models.IntegerField(verbose_name='release date')
    image = models.FileField(upload_to="Media/images")
    file = models.FileField(upload_to='Media/movie')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name