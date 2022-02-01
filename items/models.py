from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=255)


class Item(models.Model):
    nome = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)

