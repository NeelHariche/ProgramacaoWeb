from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Artigo, Like, Comentario

def artigos_list(request):
    artigos = Artigo.objects.all().order_by('-data_criacao')
    return render(request, 'artigos/list.html', {'artigos': artigos})

def artigo_detail(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    comentarios = artigo.comentarios.all().order_by('data_criacao')
    return render(request, 'artigos/detail.html', {'artigo': artigo, 'comentarios': comentarios})

@login_required
def artigo_create(request):
    if not request.user.groups.filter(name='autores').exists():
        raise PermissionDenied
    if request.method == 'POST':
        Artigo.objects.create(
            titulo=request.POST['titulo'],
            texto=request.POST['texto'],
            link_externo=request.POST.get('link_externo') or None,
            fotografia=request.FILES.get('fotografia'),
            autor=request.user,
        )
        return redirect('artigos:list')
    return render(request, 'artigos/form.html')

@login_required
def artigo_edit(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if artigo.autor != request.user:
        raise PermissionDenied
    if request.method == 'POST':
        artigo.titulo = request.POST['titulo']
        artigo.texto = request.POST['texto']
        artigo.link_externo = request.POST.get('link_externo') or None
        if request.FILES.get('fotografia'):
            artigo.fotografia = request.FILES['fotografia']
        artigo.save()
        return redirect('artigos:detail', pk=artigo.pk)
    return render(request, 'artigos/form.html', {'artigo': artigo})

@login_required
def artigo_delete(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if artigo.autor != request.user:
        raise PermissionDenied
    if request.method == 'POST':
        artigo.delete()
        return redirect('artigos:list')
    return render(request, 'artigos/confirmar_apagar.html', {'artigo': artigo})

def artigo_like(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    like, created = Like.objects.get_or_create(artigo=artigo, session_key=session_key)
    if not created:
        like.delete()
    return redirect('artigos:detail', pk=pk)

@login_required
def comentario_create(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if request.method == 'POST':
        Comentario.objects.create(
            artigo=artigo,
            autor=request.user,
            texto=request.POST['texto'],
        )
    return redirect('artigos:detail', pk=pk)