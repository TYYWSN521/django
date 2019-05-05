from django.db import models

# Create your models here.


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()

    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=50)
    hBook = models.ForeignKey("BookInfo", on_delete=models.CASCADE)

    def __str__(self):
        return self.hname

    def name(self):
        return self.hname
    name.short_desciption = "姓名"

    def skill(self):
        return self.hcontent
    skill.short_desciption = "功法"

    def sex(self):
        return self.hgender
    sex.short_desciption = "性别"


class Area(models.Model):
    title = models.CharField(max_length=30)
    parentarea = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
