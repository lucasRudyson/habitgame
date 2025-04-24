from rest_framework import viewsets
from ..models.heroi import Heroi
from ..serializer.heroiSerializer import HeroiSerializer
class heroiViewSet(viewsets.ModelViewSet):
    queryset = Heroi.objects.all()
    serializer_class = HeroiSerializer
        