from django.shortcuts import render,get_list_or_404,get_object_or_404
from .models import Category,Tag,Post
from comment.forms import CommentForm
# Create your views here.


def index(request):
    postlist = Post.objects.all()
    context = {
        'postlist': postlist
    }
    return render(request, 'blog/index.html', context)


def detail(request, id):
    post = get_object_or_404(Post,pk=id)
    post.views += 1
    post.save()
    context = {
        'post': post,
        'form': CommentForm(),
    }
    return render(request,'blog/single.html', context)


def achives(request,y,m):
    postlist = get_object_or_404(Post,create_time_year=y, create_time_month=m)
    context = {
        'postlist':postlist
    }
    return render(request, 'blog/index.html', context)


def category(request):
    postlist = get_object_or_404(Category,pk=id).post_set.all()
    context = {
        'postlist':postlist
    }
    return render(request, 'blog/index.html', context)


def tag(request):
    postlist = get_object_or_404(Tag, pk=id).post_set.all()
    context = {
        'postlist':postlist
    }
    return render(request, 'blog/index.html', context)

