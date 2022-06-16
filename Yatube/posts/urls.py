# Yatube/posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:pk>/', views.group_posts, name='group_list')
]
