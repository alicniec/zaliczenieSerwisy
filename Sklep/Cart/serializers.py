from rest_framework import serializers
from .models import Item, ItemsCart

class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ItemsCart
        fields = '__all__'