from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Domino

class DominoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domino
        fields = ['id', 'domino_pic', 'top_half', 'bottom_half']

class ListDominoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domino
        fields = ['top_half', 'bottom_half']
    