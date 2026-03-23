from django.contrib import admin

from .models import Ginasio
# Register your models here.
class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome","socios")
    ordering = ("nome","socios")
    search = ("nome",)
    
admin.site.register(Ginasio)
