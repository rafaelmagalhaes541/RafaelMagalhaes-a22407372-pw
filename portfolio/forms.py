from django import forms
from .models import Projeto, Tecnologia, Competencia, Formacao

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'data_de_realizacao', 'tecnologias', 'link']

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = ['nome', 'tipo', 'descricao', 'site', 'interesse']

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = ['nome', 'tipo', 'nivel', 'experiencia', 'projetos']

class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = ['titulo', 'tipo', 'instituicao', 'data_inicio', 'data_conclusao', 'descricao', 'aluno']