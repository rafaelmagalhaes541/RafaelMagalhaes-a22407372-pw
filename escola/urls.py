## escola/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('cursos/', views.cursos_view, name="cursos"),
    path('curso/<int:id>', views.curso_view, name="curso"),
    path('', views.cursos_view),
]