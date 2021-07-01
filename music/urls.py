from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "music"

urlpatterns = [
    # /music/
    path('', views.IndexView.as_view(), name="index"),

    # /music/register/
    path('register/', views.UserFormView.as_view(), name="register"),

    # /music/<pk>/
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),

    # /music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name="album_add"),

    # /music/album/2/
    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name="album_update"),

    # /music/album/2/delete/
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name="album_delete"),
]
