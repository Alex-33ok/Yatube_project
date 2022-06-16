from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Главная страница
def index(request):
    context = {'text':'Это главная страница проекта Yatube'}
    return render(request, 'posts/index.html', context)

def group_posts(request, slug):
    context = {'group': group, 'group_posts': group_posts}
    return render(request, 'posts/group_list.html', context)

