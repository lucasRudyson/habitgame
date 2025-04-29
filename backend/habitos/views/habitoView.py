from rest_framework import viewsets
from ..models.habito import Habito
from ..serializer.habitoSerializer import HabitoSerializer

class HabitoViewSet(viewsets.ModelViewSet):
    queryset =  Habito.objects.all()
    serializer_class = HabitoSerializer