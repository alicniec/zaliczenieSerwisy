from rest_framework import serializers
from django.contrib.auth import authenticate
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
            raise serializers.ValidationError({'email': ('Ten email już istnieje.')})
        
        if Uzytkownik.objects.filter(username = username).exists():
            raise serializers.ValidationError({"username": ('Ta nazwa już istenieje.')})

        return super().validate(data)

    def create(self, validated_data):
        return Uzytkownik.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
#     # email = serializers.CharField(max_length = 255)
#     # haslo = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = Uzytkownik
        fields = ('email', 'haslo',)

#     def validate(self, data):
#         email = data.get('email', None)
#         haslo = data.get('haslo', None)

#         if email is None:
#             raise serializers.ValidationError({'email': ('Email jest wymagany do zalogowania.')})
        
#         if haslo is None:
#             raise serializers.ValidationError({'haslo': ('Haslo jest wymagane do zalogowania.')})
        
#         user = authenticate(username=email, password=haslo)

#         if user is None:
#             raise serializers.ValidationError({'email': ('Nie ma użytkownika o tym emailu.')})
        
#         if not user.is_active:
#             raise serializers.ValidationError({'email': ('Konto jest dezaktywowane.')})
        
#         #return super().validate(data)
#         return {
#             'email': user.email,
#             'haslo': user.haslo
#         }
class UzytkownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uzytkownik
        fields = ('email', 'username', 'haslo',)
