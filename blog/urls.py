from django.urls import path
from . import views

urlpatterns = [
    path('',views.starting_page,name = 'start-page'),
    path('posts',views.posts,name = 'posts-page'),
    path('posts/<slug:slug>',views.post_detail,name = 'posts-detail-page')
]

