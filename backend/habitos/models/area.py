from django.db import models
from .heroi import Heroi



class Area(models.Model):
    ESFORCO_CHOICE = (('b','baixo'),('m','medio'),('a','alto'))
    heroi = models.ForeignKey(Heroi, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=300)
    esforco = models.CharField(max_length=2,choices=ESFORCO_CHOICE, verbose_name='Esforço para o habito')
    
    def __str__(self):
        return f'{self.titulo},{self.esforco}'
    