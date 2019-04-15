from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('home',blog.views.home, name='home'),
    path('home/post/<int:post_id>/',blog.views.detail,name='detail'),
    path('post/new/',blog.views.post_new,name='new'),
    path('post/<int:post_id>/edit', blog.views.post_edit,name='edit'),
    path('post/<int:post_id>/delete',blog.views.post_delete,name='delete'),

]