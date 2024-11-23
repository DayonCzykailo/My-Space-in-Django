from django.contrib import admin
from django.urls import path
from gallery.views import index, imagem, buscar

urlpatterns = [
    path('', index, name='home'),
    path('index', index, name='index'),
    path('imagem/<int:image_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
]