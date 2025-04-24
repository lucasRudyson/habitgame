from rest_framework import viewsets
from ..models.semana import Semana
from ..serializer.semanaSerializer import SemanaSerializer

class SemanaViewSet(viewsets.ModelViewSet):
    queryset = Semana.objects.all()
    serializer_class = SemanaSerializer