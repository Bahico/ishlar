from django.urls import path
from . import views


urlpatterns = [
    path('', views.comments, name='comments'),
    path('create/', views.commentCreate, name='comment-create'),
    path('photo/<str:id>/', views.commentPhoto, name="comment-photo"),
    path('detail/<str:id>/<str:pk>/', views.comment, name='comment-detail'),
    path('delete/<str:id>/', views.commentDelete, name='comment-delete'),
]
