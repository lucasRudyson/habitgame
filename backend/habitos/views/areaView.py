from rest_framework import viewsets
from ..serializer.areaSerializer import AreaSerializer
from ..models.area import Area


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

