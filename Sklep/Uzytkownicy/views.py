from django.shortcuts import render
from .serializers import RegistrationSerializer, UzytkownikSerializer, LoginSerializer
from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from .models import Uzytkownik
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime
# Create your views here.

class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "Message": "Użytkownik utworzony pomyślnie",
            "User": serializer.data}, status=status.HTTP_201_CREATED)
        
        #return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(generics.GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        # serializer = self.get_serializer(data=request.data)

        # if serializer.is_valid():
        #     #serializer.save()
        #     return Response({
        #         "Message": "Użytkownik zalogowany pomyślnie",
        #         "User": serializer.data}, status=status.HTTP_200_OK)
        
        # return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        email = request.data['email']
        haslo = request.data['haslo']

        user = Uzytkownik.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("Nie znaleziono użytkownika")
        
        if not user.check_password(haslo):
            raise AuthenticationFailed("Złe hasło")

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60), #czas działa tokenu
            'iat': datetime.datetime.utcnow() #kiedy token został wygenerowany
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        
        return Response({
            "message": "Pomyślnie zalogowano użytkownika.",
            'jwt': token
        })

class UzytkownikViewSet(viewsets.ModelViewSet):
    queryset = Uzytkownik.objects.all()
    serializer_class = UzytkownikSerializer