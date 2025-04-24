from rest_framework import serializers
from ..models.historicoHabito import HistoricoHabito

class HistoricoHabitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoHabito
        fields = '__all__'
