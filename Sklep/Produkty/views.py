from django.shortcuts import render
from .models import Kategoria, Produkty, Gatunki
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):

    zapytanie = Produkty.objects.all()
    return HttpResponse(zapytanie)

    kategorie = Produkty.objects.all()
    # return HttpResponse(kategoria)

    template = loader.get_template('produkty/index.html')

def kategoria(request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    return HttpResponse(kategoria_user.nazwa)



def produkt(request, id):
    produkt_user = Produkty.objects.get(pk=id)
    napis = "<h1>" + str(produkt_user) + "</h1>" + "<p>" + str(produkt_user.gatunek) + "</p>" + "<p>" + str(produkt_user.opis) + "</p>" + "<p>" + str(produkt_user.cena) + "</p>"
    return HttpResponse(napis)