## ficheiro escola/views.py

from django.shortcuts import render
from .models import Curso

def cursos_view(request):
    cursos=Curso.objects.all()       
    return render(request, 'escola/cursos.html', {'cursos': cursos})

def curso_view(request, id):
    curso=Curso.objects.get(id=id)       
    return render(request, 'escola/curso.html', {'curso': curso})