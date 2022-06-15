from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Главная страница
def index(request):
    template = 'posts/index.html'
    title= 'Это мой Title'
    context = {'title':title, 'text':'Это главная страница проекта Yatube'}
    return render(request, template, context)

def group_posts(request):
    context = {'groups': 'Здесь будет информация о группах проекта Yatube'}
    return render(context)

def group_posts_detail(request, pk):
    return HttpResponse(f'Пост номер {pk}')
