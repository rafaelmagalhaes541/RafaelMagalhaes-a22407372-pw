from django.urls import path
from . import views

urlpatterns = [
    path('', views.aluno_view, name='home'),
    path('aluno/', views.aluno_view, name='aluno'),
    path('competencia/', views.competencia_view, name='competencia'),
    path('competencia/novo/', views.competencia_create, name='competencia_create'),
    path('competencia/<int:pk>/editar/', views.competencia_update, name='competencia_update'),
    path('competencia/<int:pk>/apagar/', views.competencia_delete, name='competencia_delete'),
    path('formacao/', views.formacao_view, name='formacao'),
    path('formacao/novo/', views.formacao_create, name='formacao_create'),
    path('formacao/<int:pk>/editar/', views.formacao_update, name='formacao_update'),
    path('formacao/<int:pk>/apagar/', views.formacao_delete, name='formacao_delete'),
    path('licenciatura/', views.licenciatura_view, name='licenciatura'),
    path('makingof/', views.makingof_view, name='makingof'),
    path('professor/', views.professor_view, name='professor'),
    path('projeto/', views.projeto_view, name='projeto'),
    path('projetos/novo/', views.projeto_create, name='projeto_create'),
    path('projetos/<int:pk>/editar/', views.projeto_update, name='projeto_update'),
    path('projetos/<int:pk>/apagar/', views.projeto_delete, name='projeto_delete'),
    path('tecnologia/', views.tecnologia_view, name='tecnologia'),
    path('tecnologia/novo/', views.tecnologia_create, name='tecnologia_create'),
    path('tecnologia/<int:pk>/editar/', views.tecnologia_update, name='tecnologia_update'),
    path('tecnologia/<int:pk>/apagar/', views.tecnologia_delete, name='tecnologia_delete'),
    path('tfc/', views.tfc_view, name='tfc'),
    path('unidadecurricular/', views.unidadecurricular_view, name='unidadecurricular'),
    path('sobre/', views.sobre, name='sobre'),
]