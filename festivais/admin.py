from django.contrib import admin

from .models import Festival

# Register your models here.
class FestivalAdmin(admin.ModelAdmin):
    list_display = ("nome","tipo")
    ordering = ("nome","tipo")
    search = ("nome",)
    
admin.site.register(Festival)