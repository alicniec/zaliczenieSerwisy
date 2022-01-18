from dataclasses import field
from rest_framework import serializers
from .models import Kategoria, Produkt

class ProduktSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produkt
        fields = '__all__'

class KategoriaSerizalizers(serializers.ModelSerializer):
    class Meta:
        model = Kategoria
        fields = '__all__'