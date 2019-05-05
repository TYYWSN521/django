from django.db import models

# Create your models here.
class Question(models.Model):
    desc = models.CharField(max_length=50)
    def __str__(self):
        return self.desc

    def desctext(self):
        return self.desc
    desctext.short_description = '问题描述'
class Choice(models.Model):
    desc = models.CharField(max_length=50)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.desc
