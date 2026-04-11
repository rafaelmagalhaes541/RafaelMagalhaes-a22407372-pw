from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'duracao', 'creditos')
    search_fields = ('nome',)
    list_filter = ('duracao',)

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero', 'ano', 'licenciatura')
    search_fields = ('nome', 'numero')
    list_filter = ('ano', 'licenciatura')

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'disciplina')
    search_fields = ('nome', 'disciplina')

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'interesse')
    search_fields = ('nome', 'tipo')
    list_filter = ('tipo',)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_de_realizacao')
    search_fields = ('titulo',)
    list_filter = ('data_de_realizacao',)
    filter_horizontal = ('tecnologias',)

@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'professor', 'creditos')
    search_fields = ('nome',)
    list_filter = ('professor',)
    filter_horizontal = ('projetos',)

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'orientador', 'ano')
    search_fields = ('titulo', 'tema')
    list_filter = ('ano',)

@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'nivel', 'experiencia')
    search_fields = ('nome', 'tipo')
    list_filter = ('nivel',)
    filter_horizontal = ('projetos',)

@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'instituicao', 'aluno')
    search_fields = ('titulo', 'instituicao')
    list_filter = ('tipo',)

@admin.register(MakingOF)
class MakingOFAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'uso_ia')
    list_filter = ('uso_ia',)