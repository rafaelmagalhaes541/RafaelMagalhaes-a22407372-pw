from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .forms import ProjetoForm
from .models import *


def aluno_view(request):
    alunos = (
        Aluno.objects
        .select_related('licenciatura')
        .all()
    )
    return render(request, 'portfolio/aluno.html', {'alunos': alunos})


def competencia_view(request):
    competencias = (
        Competencia.objects
        .prefetch_related('projetos')
        .all()
    )
    return render(request, 'portfolio/competencia.html', {'competencias': competencias})


def formacao_view(request):
    formacoes = (
        Formacao.objects
        .select_related('aluno')
        .all()
    )
    return render(request, 'portfolio/formacao.html', {'formacoes': formacoes})


def licenciatura_view(request):
    licenciaturas = Licenciatura.objects.all()
    return render(request, 'portfolio/licenciatura.html', {'licenciaturas': licenciaturas})


def makingof_view(request):
    makingofs = MakingOF.objects.all()
    return render(request, 'portfolio/makingof.html', {'makingofs': makingofs})


def professor_view(request):
    professores = (
        Professor.objects
        .prefetch_related('unidades_curriculares')
        .all()
    )
    return render(request, 'portfolio/professor.html', {'professores': professores})


def projeto_view(request):
    projetos = (
        Projeto.objects
        .prefetch_related('tecnologias')
        .all()
    )
    return render(request, 'portfolio/projeto.html', {'projetos': projetos})

def projeto_create(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projeto') 
    else:
        form = ProjetoForm()

    return render(request, 'portfolio/projeto_form.html', {'form': form})

def projeto_update(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projeto')
    else:
        form = ProjetoForm(instance=projeto)

    return render(request, 'portfolio/projeto_form.html', {'form': form})

def projeto_delete(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    projeto.delete()
    return redirect('projeto')


def tecnologia_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologia.html', {'tecnologias': tecnologias})


def tfc_view(request):
    tfcs = (
        TFC.objects
        .select_related('autor', 'orientador')
        .all()
    )
    return render(request, 'portfolio/tfc.html', {'tfcs': tfcs})


def unidadecurricular_view(request):
    unidades = (
        UnidadeCurricular.objects
        .prefetch_related('professores', 'projetos')
        .all()
    )
    return render(request, 'portfolio/unidadecurricular.html', {'unidades': unidades})