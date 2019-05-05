from django.shortcuts import render
from .models import Question,Choice
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request, 'polls/index.html',{'question':Question.objects.all()})

def detail(request):
    return render(request,'polls/detail.html',{'question':Question.objects.get(pk=id)})

def vote(request):
    id = request.POST['votenum']
    choice = Choice.objects.get(pk=id)
    choice.votes += 1
    choice.save()
    return HttpResponseRedirect('/polls/result/'+str(choice.id)+'/')


def result(request, cid):
    choice = Choice.objects.get(pk=cid)
    return render(request,'/polls/result.html',{'question':choice.question})