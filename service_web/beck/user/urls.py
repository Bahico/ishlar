from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name="user-list"),
    path('me/', views.UserInformation.as_view()),
]
