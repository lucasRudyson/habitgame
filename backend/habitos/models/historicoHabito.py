from django.db import models
from .habito import Habito
class HistoricoHabito(models.Model):
    habito = models.ForeignKey(Habito,on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    completo = models.BooleanField()

    def __str__(self):
        return f'{self.habito.titulo}- {self.data}'
    