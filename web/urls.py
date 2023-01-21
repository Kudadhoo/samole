
from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('detail/<str:pk>/', views.detail, name="details"),
    path('like/<str:pk>/', views.like, name="like_post"),
]