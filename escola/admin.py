from django.contrib import admin

from .models import Escola
# Register your models here.

class EscolaAdmin(admin.ModelAdmin):
    list_display = ("nome","agrupamento")
    ordering = ("nome","agrupamento")
    search = ("nome",)
    
admin.site.register(Escola)