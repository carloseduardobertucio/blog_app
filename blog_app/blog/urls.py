from django.urls import path
from . import views
from .views import create_post

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_detail/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create-post/', create_post, name='create_post'),
]

