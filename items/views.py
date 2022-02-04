from django.shortcuts import render
from .models import Item


def index(request):
    items = Item.objects.all()
    return render(request, 'item/index.html', {
        'items': items
    })

def vw_item(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'item/vw_item.html', {
        'item': item
    })