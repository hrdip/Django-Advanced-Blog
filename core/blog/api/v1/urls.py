from django.urls import path
from . import views

app_name = "api-v1"

urlpatterns = [
    path('post/', views.postList, name='post-list'),
    path('post/<int:id>', views.postDetail, name='post-detail'),
]