from django.shortcuts import render
from django.http import HttpResponse
from gallery.models import Photo

def index(request):
    data = Photo.objects.all()



    return render(request, 'gallery/index.html', {'datas': data})

def imagem(request):
    return render(request, 'gallery/imagem.html')