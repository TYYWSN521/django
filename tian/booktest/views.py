from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo
from django.template import loader
# Create your views here.
#
#
# def index(request):
#     # return HttpResponse('首页')
#     # indextem = loader.get_template('booktest/index.html')
#     # cont = {'username': 'tyy'}
#     # result = indextem.render(cont)
#     # return HttpResponse(result)
#     return render(request, 'booktest/index.html', {'username': 'tyy'})
#
#
# def list(request):
#     # return HttpResponse('列表页')
#     b1 = BookInfo.objects.all()
#     return render(request, 'booktest/list.html', {'booklist': b1})
#
#
# def detail(request, id):
#     # try:
#     #     book = BookInfo.objects.get(pk=int(id))
#     #     return HttpResponse(book)
#     # except:
#     #     return HttpResponse('id错误')
#     book = BookInfo.objects.get(pk=id)
#     return render(request, 'booktest/detail.html', {'book':book})
# ============
def index(request):
    return render(request,'booktest/list.html',{'username': "田元元"})

def list(request):
    b1 = BookInfo.objects.all()
    return render(request,'booktest/detail.html', {'booklist': b1})

def detail(request):
    book = BookInfo.objects.get(pk=id)
    return render(request,'booktest/list.html', {'book': book})