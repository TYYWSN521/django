from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField('名称', max_length=30)

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('名称', max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('标题', max_length=10)
    summary = models.CharField('摘要', max_length=100)
    body = models.TextField('内容')
    views = models.PositiveIntegerField('阅读量', default=0)
    create_time = models.DateTimeField('发布时间', auto_now_add=True)
    modeified_time = models.DateTimeField('修改时间', auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='类别')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


#
# class Comment(models.Model):
#     name = models.
