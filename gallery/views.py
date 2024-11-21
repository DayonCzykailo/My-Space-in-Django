from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from gallery.models import Photo

def index(request):
    data = Photo.objects.all()
    #data = Photo.objects.filter(published=True)

    return render(request, 'gallery/index.html', {'datas': data})

def imagem(request, image_id):
    photo = get_object_or_404(Photo, pk=image_id)
    return render(request, 'gallery/imagem.html', {'data': photo})