from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Uzytkownik



class RegistrationSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(
    #     max_length=255,
    #     style={'input_type': 'email', 'placeholder': 'email', 'autofocus': True}
    #     )

    # username = serializers.CharField(
    #     max_length=255, read_only=True,
    #     style={'input_type': 'username', 'placeholder': 'username'}
    #     )

    haslo = serializers.CharField(
        max_length = 255, 
        min_length=8, 
        write_only=True,
        style={'input_type': 'password'}
        )
    
    token = serializers.CharField(
        max_length = 255, 
        read_only=True)
    class Meta:
        model = Uzytkownik
        fields = ('email', 'username', 'haslo', 'token')
    
    def validate(self, data):
        email = data.get('email', None)
        username = data.get('username', None)

        if Uzytkownik.objects.filter(email = email).exists():
            raise serializers.ValidationError({'email': ('Ten email już istnieje.')})
        
        if Uzytkownik.objects.filter(username = username).exists():
            raise serializers.ValidationError({"username": ('Ta nazwa już istenieje.')})

        return super().validate(data)

    def create(self, validated_data):
        return Uzytkownik.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255, style={'input_type': 'email'})
    haslo = serializers.CharField(max_length=255, write_only=True, style={'input_type': 'password'})

    class Meta:
        model = Uzytkownik
        fields = ('email', 'haslo',)


class UzytkownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uzytkownik
        fields = ('email', 'username', 'haslo', 'token')
