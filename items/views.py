from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Item
from django.core.paginator import Paginator
from django.db.models import Q


def index(request):
    items = Item.objects.order_by('nome').filter(ocultar=False)
    paginator = Paginator(items, 10)

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

def busca(request):
    busca = request.GET.get('busca')

    if busca is None:
        raise Http404()

    items = Item.objects.order_by('nome').filter(
        Q(nome__icontains=busca) 
    )

    paginator = Paginator(items, 10)

    page = request.GET.get('page')
    items = paginator.get_page(page)
    return render(request, 'item/busca.html', {
        'items': items
    })