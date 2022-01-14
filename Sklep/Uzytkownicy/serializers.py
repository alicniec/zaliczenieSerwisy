from rest_framework import serializers
from .models import Uzytkownik

class RegistrationSerializer(serializers.ModelSerializer):

    haslo = serializers.CharField(
        max_length = 255, 
        min_length=8, 
        write_only=True)
    class Meta:
        model = Uzytkownik
        fields = ('email', 'username', 'haslo',)
    
    def validate(self, data):
        email = data.get('email', None)
        username = data.get('username', None)

        if Uzytkownik.objects.filter(email = email).exists():
            raise serializers.ValidationError({'email': ('email already exists')})
        
        if Uzytkownik.objects.filter(username = username).exists():
            raise serializers.ValidationError({'username': ('username already exists')})

        return super().validate(data)

    def create(self, validated_data):
        return Uzytkownik.objects.create_user(**validated_data)

class UzytkownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uzytkownik
        fields = ('email', 'username', 'haslo',)
