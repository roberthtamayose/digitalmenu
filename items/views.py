from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Item
from django.core.paginator import Paginator


def index(request):
    items = Item.objects.all()
    paginator = Paginator(items, 2)

    page = request.GET.get('page')
    items = paginator.get_page(page)
    return render(request, 'item/index.html', {
        'items': items
    })

def vw_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'item/vw_item.html', {
        'item': item
    })