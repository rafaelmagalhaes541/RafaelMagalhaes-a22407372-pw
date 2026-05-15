from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Artigo, Like
from .forms import ArtigoForm, ComentarioForm


def is_autor(user):
    return user.is_authenticated and user.groups.filter(name='autores').exists()


def artigo_list(request):
    artigos = Artigo.objects.all().order_by('-data_criacao')

    return render(request, 'artigos/list.html', {
        'artigos': artigos,
        'is_autor': is_autor(request.user)
    })


@login_required
def artigo_create(request):
    if not is_autor(request.user):
        return redirect('artigo_list')

    form = ArtigoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user
        artigo.save()
        return redirect('artigo_list')

    return render(request, 'artigos/form.html', {'form': form})


@login_required
def artigo_update(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)

    if artigo.autor != request.user:
        return redirect('artigo_list')

    form = ArtigoForm(request.POST or None, request.FILES or None, instance=artigo)

    if form.is_valid():
        form.save()
        return redirect('artigo_list')

    return render(request, 'artigos/form.html', {'form': form})


def like_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)

    if request.user.is_authenticated:
        like, created = Like.objects.get_or_create(
            artigo=artigo,
            user=request.user
        )
        if not created:
            like.delete()

    return redirect('artigo_list')


@login_required
def comentar(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)

    form = ComentarioForm(request.POST)

    if form.is_valid():
        comentario = form.save(commit=False)
        comentario.user = request.user
        comentario.artigo = artigo
        comentario.save()

    return redirect('artigo_list')