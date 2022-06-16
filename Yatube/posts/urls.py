# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('group/', views.group_posts),
    path('group/<slug:pk>/', views.group_posts_detail, name='group list')
]
