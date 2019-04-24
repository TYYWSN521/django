from django import template
from ..models import Post,Category,Tag

register= template.Library()


@register.simple_tag
def getlatestposts(num=3):
    return Post.objects.all().order_by('-create_time')[:num]


@register.simple_tag
def getdatelist(num=3):
    return Post.objects.dates('create_time','month',order='DESC')[:num]


@register.simple_tag
def getcatgory():
    return Category.objects.all()


@register.simple_tag
def gettags():
    return Tag.objects.all()
