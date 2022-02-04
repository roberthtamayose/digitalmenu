from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>', views.vw_item, name='vw_item'),
]