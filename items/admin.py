from django.contrib import admin
from .models import Categoria, Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria')
    list_display_links = ('nome','categoria')
    list_filter = ('nome','categoria')
    list_per_page = 10


admin.site.register(Categoria)
admin.site.register(Item, ItemAdmin)