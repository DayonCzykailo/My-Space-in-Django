from django.contrib import admin
from django.urls import path
from apps.gallery.views import index, imagem, buscar, new_image, edit_image, delete_image

urlpatterns = [
    path('', index, name='home'),
    path('index', index, name='index'),
    path('imagem/<int:image_id>', imagem, name='imagem'),
    path('new_image', new_image, name='new_image'),
    path('edit_image', edit_image, name='edit_image'),
    path('delete_image/<int:id>', delete_image, name='delete_image'),
    path('buscar', buscar, name='buscar'),
]