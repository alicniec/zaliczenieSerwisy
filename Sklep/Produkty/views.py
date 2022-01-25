from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework import status, generics

from .serializers import *
from .models import *

# Create your views here.
class ProduktView(APIView):

    serializer_class = ProduktSerializer
    renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'produkty/login.html'

    def index(request):
        kategoria = Kategoria.objects.all()
        produkt_user = Produkt.objects.all()

        dane = {'kategoria' : kategoria, 'produkt_user': produkt_user}
        return render(request, 'produkty/index.html', dane)

    def produkt(request, id):
        produkt_user = Produkt.objects.get(pk=id)
        kategoria = Kategoria.objects.all()

        dane = {'produkt_user' : produkt_user, 'kategoria' : kategoria}

        return render(request, 'produkty/produkt.html', dane)

    def kategoria(request, id):
        kategoria_user = Kategoria.objects.get(pk=id)
        kategoria_produkt = Produkt.objects.filter(kategoria = kategoria_user)
        kategoria = Kategoria.objects.all()
        dane = {'kategoria_user' : kategoria_user, 'kategoria_produkt': kategoria_produkt, 'kategoria':kategoria}
        return render(request, 'produkty/kategoria.html', dane)

    def kontakt(request):
        kategoria = Kategoria.objects.all()
        dane = {'kategoria' : kategoria}
        return render(request, 'produkty/kontakt.html', dane)

    



    
