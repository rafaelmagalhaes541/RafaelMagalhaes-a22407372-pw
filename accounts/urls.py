from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registo/', views.registo_view, name='registo'),
    path('magic/', views.login_magic_link, name='magic_request'),
    path('magic-login/', views.magic_login, name='magic_login'),
]