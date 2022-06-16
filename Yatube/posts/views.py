from django.shortcuts import render, get_object_or_404
from .models import Post, Group
COUNT_RECORDS: int = 10
def index(request):
    posts = Post.objects.select_related('author', 'group').all()[:COUNT_RECORDS]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    group_posts = group.posts.all()[:COUNT_RECORDS]
    context = {
        'group': group,
        'group_posts': group_posts,
    }
    return render(request, 'posts/group_list.html', context)

