# movies/models.py

from django.db import models
# Comment 모델을 가져옴
from post.forms import Comment


class Movie(models.Model):
    api_id = models.IntegerField(default=-1)
    title = models.CharField(max_length=200)
    overview = models.TextField()
    release_date = models.DateField()
    poster_url = models.URLField()

    def __str__(self):
        return self.title

