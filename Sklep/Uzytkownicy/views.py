from django.shortcuts import render, redirect

from Produkty.models import Produkt
from .serializers import RegistrationSerializer, UzytkownikSerializer, LoginSerializer
from .models import Uzytkownik
from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers

from django.contrib.auth import login

from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView




class RegistrationAPIView(APIView):

    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'uzytkownicy/register.html'

    def get(self, request):
        return Response({'serializer': self.serializer_class})


    def post(self, request):
        serializer = self.serializer_class(data = request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        # return Response({
        #     "Message": "Użytkownik utworzony pomyślnie",
        #     "User": serializer.data}, status=status.HTTP_201_CREATED)

        return redirect("login")

        
        
        #return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(generics.GenericAPIView):

    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'uzytkownicy/login.html'


    def get(self, request):
        return Response({'serializer': self.serializer_class})

    def post(self, request):
        
        email = request.POST.get('email')
        haslo = request.POST.get('haslo')

        # email = request.data['email']
        # haslo = request.data['haslo']

        user = authenticate(username = email, password=haslo)

        if user is None:
            raise AuthenticationFailed("Nie znaleziono użytkownika")

        if not user.check_password(haslo):
            raise AuthenticationFailed("Złe hasło")
            #redirect("login")
        
        if not user.is_active:
            raise serializers.ValidationError('Ten użytkownik jest nieaktywny.')
            
        # return Response({
        #     "message": "Pomyślnie zalogowano użytkownika.",
        #     'jwt': user.token
        # })

        return redirect("base")



class UzytkownikViewSet(viewsets.ModelViewSet):
    queryset = Uzytkownik.objects.all()
    serializer_class = UzytkownikSerializer
