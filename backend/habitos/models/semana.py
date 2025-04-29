from django.db import models
from .habito import Habito

class Semana(models.Model):
    habito = models.ForeignKey(Habito,on_delete=models.CASCADE)
    segunda = models.BooleanField(default=False)
    terça = models.BooleanField(default=False)
    quarta = models.BooleanField(default=False)
    quinta = models.BooleanField(default=False)
    sexta = models.BooleanField(default=False)
    sabado = models.BooleanField(default=False)
    domingo = models.BooleanField(default=False)
