from django.db import models


class Post(models.Model):
    content = models.TextField(default="", blank=True)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField('users.User', related_name='likes', through='PostLike')


class PostLike(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    like_date = models.DateField(auto_now_add=True)
