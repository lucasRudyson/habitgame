from rest_framework import viewsets
from ..models.historicoHabito import HistoricoHabito
from ..serializer.historicoHabitoSerializer import HistoricoHabitoSerializer

class HistoricoHabitoViewSet(viewsets.ModelViewSet):
    queryset = HistoricoHabito.objects.all()
    serializer_class = HistoricoHabitoSerializer