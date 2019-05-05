from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import BookInfo,HeroInfo, Area
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
    return render(request,'booktest/index.html', {'username': "田元元"})


def list(request):
    b1 = BookInfo.objects.all()
    return render(request,'booktest/list.html', {'booklist': b1})


def detail(request, id):
    book = BookInfo.objects.get(pk=id)
    return render(request,'booktest/detail.html', {'book': book})


def delete(request, id):
    try:
        BookInfo.objects.get(pk=id).delete()
        b1 = BookInfo.objects.all()
        return render(request, 'booktest/list.html', {'booklist': b1})
    except:
        print("删除失败")


def addhero(request, bookid):
    try:
        return render(request, 'bookteset/addhero.html',{'bookid': bookid})

    except:
        return HttpResponse("添加失败")


def addherohandler(request,bookid):
    try:
        bookid = request.POST('bookid')
        hname = request.POST('heroname')
        hgender = request.POST('sex')
        hcontent = request.POST('herocontent')

        book = BookInfo.objects.get(pk=bookid)
        hero = HeroInfo()
        hero.hname = hname
        hero.hgender = True
        hero.hcontent = hcontent
        hero.hBook = book
        hero.save()
        return HttpResponse('/booktest/detail'+str(bookid)+'/',{'book':'book'})
    except:
        return HttpResponse("添加失败")


def area(request):
    area = Area.objects.get(pk=3)
    return render(request, 'booktest/area.html', {'area':area})
