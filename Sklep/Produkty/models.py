from distutils.command.upload import upload
from operator import mod
from re import T
from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, default=True)

    # def get_absolute_url(self):
    #     return reverse('store:category:list', args=[self.slug])

    def __str__(self):
        return self.nazwa + " "
    


class Produkt(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    gatunek = models.CharField(max_length=100)
    kategoria = models.ForeignKey(Kategoria, related_name='produkt', on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='images/', default=True)
    slug = models.SlugField(max_length=255, unique=True, default=True)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + " "

    