from django.db import models
from .heroi import Heroi
from .area import Area


class Habito(models.Model):
    heroi = models.ForeignKey(Heroi,on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=300)
    descricao = models.TextField()
    frequencia = models.IntegerField(default=0,editable=False)

    def __str__(self):
        return f'O {self.titulo}'
    