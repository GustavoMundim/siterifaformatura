from django.contrib import admin
from .models import Sorteio, RifaTexto
# Register your models here.

@admin.register(Sorteio)
class AdminView(admin.ModelAdmin):
    list_display = ('nome','sobrenome','numero_rifa', 'aprovado')
    search_fields = ('nome','sobrenome')
    list_editable = ('aprovado',)

admin.site.register(RifaTexto)
