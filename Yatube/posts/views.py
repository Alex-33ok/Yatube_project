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
    template = 'posts/group_list.html'
    title= 'Здесь будет информация о группах проекта Yatube ЧЛЕН'
    context = {'title': title}
    return render(request, template, context)

def group_posts_detail(request, pk):
    return HttpResponse(f'Пост номер {pk}')
