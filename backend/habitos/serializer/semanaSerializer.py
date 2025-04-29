from rest_framework import serializers
from ..models.semana import Semana

class SemanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semana
        fields = '__all__'
