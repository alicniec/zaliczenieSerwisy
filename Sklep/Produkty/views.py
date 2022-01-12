from django.shortcuts import render
from .models import Kategoria, Produkty, Gatunki
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):

    zapytanie = Produkty.objects.all()
    kategorie = Kategoria.objects.all()

    dane = {
        'kategorie' : kategorie,
        'zapytanie' : zapytanie
    }

    return render(request, 'produkty/index.html', dane)


def kategoria(request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    return HttpResponse(kategoria_user.nazwa)


def produkt(request, id):
    produkt_user = Produkty.objects.get(pk=id)
    dane = {'produkt_user' : produkt_user}
    return render(request, 'produkty/produkt.html', dane)