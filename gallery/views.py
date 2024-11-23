from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from gallery.models import Photo

def index(request):
    if request.user.is_authenticated:

        data = Photo.objects.all()
        #data = Photo.objects.filter(published=True)

        return render(request, 'gallery/index.html', {'datas': data})
    
    return redirect('login')

def imagem(request, image_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    photo = get_object_or_404(Photo, pk=image_id)
    return render(request, 'gallery/imagem.html', {'data': photo})

def buscar(request):
    if not request.user.is_authenticated:
        return redirect('login')

    fotografias = Photo.objects.order_by("title").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/buscar.html", {"cards": fotografias})