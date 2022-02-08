from django.contrib import admin
from .models import Categoria, Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'categoria', 'ocultar')
    list_filter = ('categoria','ocultar')
    list_editable = ('categoria', 'ocultar')
    list_per_page = 20


admin.site.register(Categoria)
admin.site.register(Item, ItemAdmin)