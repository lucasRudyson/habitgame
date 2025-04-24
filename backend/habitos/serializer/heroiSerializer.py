from rest_framework import serializers
from ..models.heroi import Heroi


class HeroiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heroi
        fields = '__all__'
        