# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group_posts', views.group_posts_list),
    path('group_posts/<slag:slag>/', views.group_posts_detail)
            ]