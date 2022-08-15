from django.urls import path

from . import views

urlpatterns = [
    path('photo-del/', views.userDelPhoto),
    # path('image/<str:id>', views.userImageUser),
    path('image-id/', views.userImageId),
    path('image-edit/', views.userImageEdit),
    path('information/', views.userInformationView),
    path('author/', views.userAuthor),
    path('update/', views.userUpdate),
    path('id/', views.userIdView),
]

