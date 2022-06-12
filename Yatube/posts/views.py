from django.http import HttpResponse
from django.shortcuts import render

# Главная страница
def index(request):
    template = 'posts/index.html'
    return render(request, template)

def group_posts(request):
    return HttpResponse('Список постов')

def group_posts_detail(request, pk):
    return HttpResponse(f'Пост номер {pk}')
