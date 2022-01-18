from rest_framework import viewsets
from . import models
from . import serializers

class ProduktViewset(viewsets.ModelViewSet):
    queryset = models.Produkt.objects.all()
    serializer_class = serializers.ProduktSerializer