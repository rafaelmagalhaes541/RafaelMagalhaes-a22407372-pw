from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm
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

def competencia_create(request):
    if request.method == 'POST':
        form = CompetenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('competencia')
    else:
        form = CompetenciaForm()

    return render(request, 'portfolio/form.html', {
    'form': form,
    'titulo': '➕ Nova Competência',
    'subtitulo': 'Regista uma competência',
    'voltar_url': '/portfolio/competencia/'
    })

def competencia_update(request, pk):
    competencia = get_object_or_404(Competencia, pk=pk)

    if request.method == 'POST':
        form = CompetenciaForm(request.POST, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect('competencia')
    else:
        form = CompetenciaForm(instance=competencia)

    return render(request, 'portfolio/form.html', {
    'form': form,
    'titulo': '✏️ Editar Competência',
    'subtitulo': 'Atualiza a competência',
    'voltar_url': '/portfolio/competencia/'
    })

def competencia_delete(request, pk):
    competencia = get_object_or_404(Competencia, pk=pk)
    competencia.delete()
    return redirect('competencia')


def formacao_view(request):
    formacoes = (
        Formacao.objects
        .select_related('aluno')
        .all()
    )
    return render(request, 'portfolio/formacao.html', {'formacoes': formacoes})

def formacao_create(request):
    if request.method == 'POST':
        form = FormacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formacao')
    else:
        form = FormacaoForm()

    return render(request, 'portfolio/form.html', {
    'form': form,
    'titulo': '➕ Nova Formação',
    'subtitulo': 'Adiciona formação académica',
    'voltar_url': '/portfolio/formacao/'
    })

def formacao_update(request, pk):
    formacao = get_object_or_404(Formacao, pk=pk)

    if request.method == 'POST':
        form = FormacaoForm(request.POST, instance=formacao)
        if form.is_valid():
            form.save()
            return redirect('formacao')
    else:
        form = FormacaoForm(instance=formacao)

    return render(request, 'portfolio/form.html', {
        'form': form,
        'titulo': '✏️ Editar Formação',
        'subtitulo': 'Atualiza a formação selecionada',
        'voltar_url': '/portfolio/formacao/'
    })

def formacao_delete(request, pk):
    formacao = get_object_or_404(Formacao, pk=pk)
    formacao.delete()
    return redirect('formacao')


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

    return render(request, 'portfolio/form.html', {
        'form': form,
        'titulo': '➕ Novo Projeto',
        'subtitulo': 'Cria um novo projeto',
        'voltar_url': '/portfolio/projeto/'
    })

def projeto_update(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projeto')
    else:
        form = ProjetoForm(instance=projeto)

    return render(request, 'portfolio/form.html', {
        'form': form,
        'titulo': '✏️ Editar Projeto',
        'subtitulo': 'Atualiza os detalhes do projeto',
        'voltar_url': '/portfolio/projeto/'
    })

def projeto_delete(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    projeto.delete()
    return redirect('projeto')


def tecnologia_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologia.html', {'tecnologias': tecnologias})

def tecnologia_create(request):
    if request.method == 'POST':
        form = TecnologiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tecnologia')
    else:
        form = TecnologiaForm()

    return render(request, 'portfolio/form.html', {
        'form': form,
        'titulo': '➕ Nova Tecnologia',
        'subtitulo': 'Adiciona uma tecnologia ao portfólio',
        'voltar_url': '/portfolio/tecnologia/'
    })

def tecnologia_update(request, pk):
    tecnologia = get_object_or_404(Tecnologia, pk=pk)

    if request.method == 'POST':
        form = TecnologiaForm(request.POST, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect('tecnologia')
    else:
        form = TecnologiaForm(instance=tecnologia)

    return render(request, 'portfolio/form.html', {
        'form': form,
        'titulo': '✏️ Editar Tecnologia',
        'subtitulo': 'Altera os dados da tecnologia',
        'voltar_url': '/portfolio/tecnologias/'
    })

def tecnologia_delete(request, pk):
    tecnologia = get_object_or_404(Tecnologia, pk=pk)
    tecnologia.delete()
    return redirect('tecnologia')


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

def sobre(request):
    return render(request, 'portfolio/sobre.html')