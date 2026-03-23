from django.contrib import admin

from .models import Receita
# Register your models here.
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ("nome","duracao")
    ordering = ("nome","duracao")
    search = ("nome",)
    
admin.site.register(Receita)