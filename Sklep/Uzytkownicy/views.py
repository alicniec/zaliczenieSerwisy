from django.shortcuts import render, redirect
from django.contrib import messages
from .serializers import RegistrationSerializer, UzytkownikSerializer, LoginSerializer
from .models import Uzytkownik
from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers

from django.contrib.auth import login

from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate



class RegistrationAPIView(generics.GenericAPIView):

    permission_classes = (AllowAny,)
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

    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        
        email = request.data['email']
        haslo = request.data['haslo']

        user = authenticate(username = email, password=haslo)

        if user is None:
            raise AuthenticationFailed("Nie znaleziono użytkownika")

        if not user.check_password(haslo):
            raise AuthenticationFailed("Złe hasło")
        
        if not user.is_active:
            raise serializers.ValidationError('Ten użytkownik jest nieaktywny.')

        return Response({
            "message": "Pomyślnie zalogowano użytkownika.",
            'jwt': user.token
        })

class UzytkownikViewSet(viewsets.ModelViewSet):
    queryset = Uzytkownik.objects.all()
    serializer_class = UzytkownikSerializer






# def homeUser(request):
#     return render(request, "uzytkownicy/homeUser.html")
    

# def RegisterView(request):
#     if request.method == "POST":

#         email = request.POST['email']
#         username = request.POST['username']
#         haslo = request.POST['haslo']
        
#         if Uzytkownik.objects.filter(email = email).exists():
#             raise serializers.ValidationError({'email': ('Ten email już istnieje.')})
        
#         if Uzytkownik.objects.filter(username = username).exists():
#             raise serializers.ValidationError({"username": ('Ta nazwa już istenieje.')})

#         user = Uzytkownik.objects.create_user(email, haslo)
#         user.save()

#         messages.success(request, "Utworzono")

#         return redirect("/api/user/login")
        
    
#     return render(request, "uzytkownicy/register.html")

# def LoginView(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         haslo = request.POST['haslo']

#         user = Uzytkownik.objects.filter(email=email).first()

#         if user is None:
#             # raise AuthenticationFailed("Nie znaleziono użytkownika")
#             messages.error(request, "Nie ma uzytkownika o tym adresie email.")
#         else:
#             if not user.check_password(haslo):
#                 # raise AuthenticationFailed("Złe hasło")
#                 messages.error(request, "Złe hasło.")
#             else:
#                 login(request, user)
#                 return render(request, "index.html")
#                 #return redirect()

#         # payload = {
#         #     'id': user.id,
#         #     'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60), #czas działa tokenu
#         #     'iat': datetime.datetime.utcnow() #kiedy token został wygenerowany
#         # }

#         # token = jwt.encode(payload, 'secret', algorithm='HS256')
        
#         # return Response({
#         #     "message": "Pomyślnie zalogowano użytkownika.",
#         #     'jwt': token
#         # })

#     return render(request, "uzytkownicy/login.html")

# class LoginAPIView(generics.GenericAPIView):

#     serializer_class = LoginSerializer

#     def post(self, request):
#         # serializer = self.get_serializer(data=request.data)

#         # if serializer.is_valid():
#         #     #serializer.save()
#         #     return Response({
#         #         "Message": "Użytkownik zalogowany pomyślnie",
#         #         "User": serializer.data}, status=status.HTTP_200_OK)
        
#         # return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#         email = request.data['email']
#         haslo = request.data['haslo']

#         user = Uzytkownik.objects.filter(email=email).first()

#         if user is None:
#             raise AuthenticationFailed("Nie znaleziono użytkownika")
        
#         if not user.check_password(haslo):
#             raise AuthenticationFailed("Złe hasło")

#         payload = {
#             'id': user.id,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60), #czas działa tokenu
#             'iat': datetime.datetime.utcnow() #kiedy token został wygenerowany
#         }

#         token = jwt.encode(payload, 'secret', algorithm='HS256')
        
#         return Response({
#             "message": "Pomyślnie zalogowano użytkownika.",
#             'jwt': token
#         })
