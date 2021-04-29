from django.urls import path, include
from . import views

app_name = 'Blog_API'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('create_blog/', views.CreateBlog.as_view(), name='create_blog'),
    path('blog_details/<slug:slug>/', views.blog_details, name='blog_details'),
    path('like/<pk>/', views.like, name='like'),
    path('dislike/<pk>/', views.dislike, name='dislike'),
    path('my_blogs/', views.MyBlogs.as_view(), name='my_blogs'),
    path('edit_blog/<pk>/', views.EditBlog.as_view(), name='edit_blog'),
]
