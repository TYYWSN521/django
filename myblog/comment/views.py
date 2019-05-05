from django.shortcuts import render,get_object_or_404,redirect,HttpResponse,reverse
from blog.models import Post
from .forms import CommentForm
# Create your views here.


def commitcomment(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(reverse('blog:detail', args=(id,)))
        else:
            return HttpResponse('评论失败')

    else:
        return HttpResponse('评论失败')
