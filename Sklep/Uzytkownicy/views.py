from django.shortcuts import render
from .serializers import RegistrationSerializer, UzytkownikSerializer
from rest_framework import status, generics, viewsets, serializers
from rest_framework.response import Response
from .models import Uzytkownik
# Create your views here.

class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "Message": "Użytkownik utworzony pomyślnie",
                "User": serializer.data}, status=status.HTTP_201_CREATED)
        
        #return Response({"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)

class UzytkownikViewSet(viewsets.ModelViewSet):
    queryset = Uzytkownik.objects.all()
    serializer_class = UzytkownikSerializer