from django.urls import path
from . import views

urlpatterns = [
    path('', views.artigo_list, name='artigo_list'),
    path('novo/', views.artigo_create, name='artigo_create'),
    path('editar/<int:pk>/', views.artigo_update, name='artigo_update'),
    path('like/<int:pk>/', views.like_artigo, name='like_artigo'),
    path('comentario/<int:pk>/', views.comentar, name='comentar'),
]