from django.shortcuts import render
from .models import Produkty
from django.http import HttpResponse

# Create your views here.

def index(request):
    zapytanie = Produkty.objects.all()
    return HttpResponse(zapytanie)