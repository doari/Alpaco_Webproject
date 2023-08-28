from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    api_id = models.IntegerField(default=-1)
    title = models.CharField(max_length=200)
    overview = models.TextField()
    release_date = models.DateField()
    poster_url = models.URLField()

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='comments')  # related_name 추가
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
