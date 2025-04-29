from django.db import models

class Heroi(models.Model):
    nome = models.CharField(max_length=300)
    xp = models.FloatField(default=0, editable=False)
    forca = models.FloatField(default=0,editable=False)
    inteligencia = models.FloatField(default=0,editable=False)
    carisma = models.FloatField(default=0,editable=False)

    def __str__(self):
        return f'{self.nome}'
    