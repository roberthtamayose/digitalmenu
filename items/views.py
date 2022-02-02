from django.shortcuts import render
from .models import Item


def index(request):
    items = Item.objects.all()
    return render(request, 'item/index.html', {
        'items': items
    })
