from django.db import models
from blog.models import Post
# Create your models here.


class Comment(models.Model):
    name = models.CharField('名字', max_length=20)
    email = models.EmailField(blank=True, null=True)
    url = models.URLField(blank=True,null=True)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
