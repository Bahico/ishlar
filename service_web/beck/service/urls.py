
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('service/<str:pk>/', views.taskList, name="task-list"),
    path('detail/<str:pk>/', views.taskDetail, name="task-detail"),
    path('create/', views.taskCreate, name="task-create"),
    path('photo/<str:pk>/', views.taskPhoto, name="task-photo"),
    path('update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('delete/<str:pk>/', views.taskDelete, name="task-delete"),
    path('views/<str:pk>/', views.taskViews, name="task-views"),
    path('like-add/<str:pk>/', views.taskLike, name='task-like-add'),
    path('like-del/<str:pk>/', views.taskLike_, name='task-like-del'),
    path('dislike-add/<str:pk>/', views.taskDisLike, name='task-dislike-add'),
    path('dislike-del/<str:pk>/', views.taskDisLike_, name='task-dislike-del'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
