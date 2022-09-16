# Create your views here.
from django.shortcuts import render

from blog.models import Post


def post_list(request):
    posts = Post.objects.prefetch_related('comments').select_related('user').order_by()
    context = {"posts": posts}
    return render(request, 'blog/posts/list.html', context=context)


def post_detail(request, pk):
    posts = Post.objects.select_related('user')
    post = posts.get(id=pk)
    context = {"post": post}
    return render(request, 'blog/posts/detail.html', context=context)
