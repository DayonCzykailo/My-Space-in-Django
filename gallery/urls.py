from django.contrib import admin
from django.urls import path
from gallery.views import index, imagem
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('imagem/', imagem, name='imagem'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)