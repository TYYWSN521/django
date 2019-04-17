from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo
from django.template import loader
# Create your views here.


def index(request):
    # return HttpResponse('首页')
    indextem = loader.get_template('booktest/index.html')
    cont = {'username': 'tyy'}
    result = indextem.render(cont)
    return HttpResponse(result)


def list(request):
    return HttpResponse('列表页')


def detail(request, id):
    try:
        book = BookInfo.objects.get(pk=int(id))
        return HttpResponse(book)
    except:
        return HttpResponse('id错误')
