from rest_framework import serializers
from ..models.habito import Habito

class HabitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habito
        fields = '__all__'

    