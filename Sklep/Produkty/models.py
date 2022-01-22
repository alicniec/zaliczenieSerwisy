from distutils.command.upload import upload
from operator import mod
from re import T
from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import BaseUserManager

# Create your models here.
#test

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=100)
    def __str__(self):
        return self.nazwa + " "

class Produkt(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    gatunek = models.CharField(max_length=100)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    zdjecia = models.ImageField(upload_to='home/')
    def __str__(self):
        return self.nazwa + " "

    