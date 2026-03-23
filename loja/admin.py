from django.contrib import admin

from .models import Loja

# Register your models here.
class LojaAdmin(admin.ModelAdmin):
    list_display = ("nome","localidade")
    ordering = ("nome","localidade")
    search = ("nome","localidade",)
    
admin.site.register(Loja)