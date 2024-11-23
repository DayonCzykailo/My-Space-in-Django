from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from apps.gallery.models import Photo
from apps.gallery.forms import PhotoForms
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
def new_image(request):
    form = PhotoForms(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            if form.save():
                messages.success(request, 'Imagem cadastrada com sucesso!')
                return redirect('index')
            else:
                messages.error(request, 'Erro ao cadastrar a imagem!')
        else:
            messages.error(request, 'Erro ao cadastrar a imagem!')


    return render(request, 'gallery/new_image.html', {'form': form})

@login_required
def edit_image(self):
    pass

@login_required
def delete_image(self, id):
    photo = Photo.objects.get(id=id)
    photo.delete()
    return redirect('index')

@login_required
def buscar(request):
    fotografias = Photo.objects.order_by("title").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/buscar.html", {"cards": fotografias})

