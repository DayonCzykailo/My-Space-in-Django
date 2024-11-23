from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from gallery.models import Photo
from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    data = Photo.objects.all()
    #data = Photo.objects.filter(published=True)
    return render(request, 'gallery/index.html', {'datas': data})
    

@login_required
def imagem(request, image_id):
    photo = get_object_or_404(Photo, pk=image_id)
    return render(request, 'gallery/imagem.html', {'data': photo})

@login_required
def buscar(request):
    fotografias = Photo.objects.order_by("title").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/buscar.html", {"cards": fotografias})