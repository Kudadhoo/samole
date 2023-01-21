from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="this is title")
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    post_date = models.DateField(auto_now_add=True, null=True)
    likes = models.IntegerField( default=0)
    body = models.TextField()

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return str(self.user)

