from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
    # Добавьте другие URL-адреса здесь
]
