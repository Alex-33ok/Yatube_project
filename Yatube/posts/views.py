from django.shortcuts import render
from django.http import HttpResponse

# Главная страница
def index(request):
    return HttpResponse('Главная страница')

# Страница со списком мороженого
def group_posts_list(request):
    return HttpResponse('Список постов')

def group_posts_detail(request, pk):
    return HttpResponse(f'Пост номер {pk}')