from django.http import QueryDict
from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ItemSerializer, CartSerializer
from .models import ItemsCart, Item
from Uzytkownicy.models import Uzytkownik

# Create your views here.

class UserCart(viewsets.ViewSet):

    # user_profile = Uzytkownik.objects.get(pk=id)
    # user_items = ItemsCart.objects.get(owner=user_profile)
    queryset = ItemsCart.objects.all()
    serializer_class = CartSerializer


    # def get(request, id):
    #     user_profile = Uzytkownik.objects.get(pk=id)
    #     user_items = ItemsCart.objects.get(owner=user_profile)
    #     print(user_profile, user_items)
    #     dane = {'user_prifile' : user_profile, 'user_items' : user_items}
    #     return render(request, 'items/item.html', dane)