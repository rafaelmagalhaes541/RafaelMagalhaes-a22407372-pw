from django.urls import path
from . import views

urlpatterns = [
    path('aluno/', views.aluno_view, name='aluno'),
    path('competencia/', views.competencia_view, name='competencia'),
    path('formacao/', views.formacao_view, name='formacao'),
    path('licenciatura/', views.licenciatura_view, name='licenciatura'),
    path('makingof/', views.makingof_view, name='makingof'),
    path('professor/', views.professor_view, name='professor'),
    path('projeto/', views.projeto_view, name='projeto'),
    path('tecnologia/', views.tecnologia_view, name='tecnologia'),
    path('tfc/', views.tfc_view, name='tfc'),
    path('unidadecurricular/', views.unidadecurricular_view, name='unidadecurricular'),
]