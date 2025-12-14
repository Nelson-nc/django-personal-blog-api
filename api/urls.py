from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="home"),
    path('posts/', views.view_post, name="view_post"),
    path('posts/create/', views.create_post, name="create_post"),
    path('posts/update/<slug:slug>/', views.update_post, name="update_post"),
    path('posts/delete/<slug:slug>', views.delete_post, name="delete_post"),

    path('comments/create/', views.create_comment, name="create_comment"),
    path('comments/post/<slug:slug>/', views.view_post_comment, name="view_post_comment"),
    path('comments/post/<slug:slug>/update/<int:pk>/', views.update_comment, name="update_comment"),
    path('comments/post/<slug:slug>/delete/<int:pk>/', views.delete_comment, name="delete_comment"),

    path('tags/all/', views.display_tags, name="display_tags")
]