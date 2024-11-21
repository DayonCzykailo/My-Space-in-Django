from django.contrib import admin
from django.urls import path
from gallery.views import index, imagem

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('imagem/', imagem, name='imagem'),
]