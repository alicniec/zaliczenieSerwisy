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
        produkt = Produkt.objects.all()
        dane = {'produkt' : produkt}
        return render(request, 'produkt/index.html', dane)

    def produkt(request, id):
        produkt_user = Produkt.objects.get(pk=id)
        return HttpResponse(produkt_user.nazwa)

    def kategoria(request, id):
        kategoria_user = Kategoria.objects.get(pk=id)
        return HttpResponse(kategoria_user.nazwa)
