from django.db import models

# Create your models here.
# hej heje hehejejej


class Gatunki(models.Model):

    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa + " "
    #wyświetlanie nazw

    class Meta:
        verbose_name = "Gatunek"
        verbose_name_plural = "Gatunki"

class Kategoria(models.Model):

    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa + " "
    #wyświetlanie nazw

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"


class Produkty(models.Model):

    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE, null=True, blank=True)
    gatunek = models.ForeignKey(Gatunki, on_delete=models.CASCADE, null=True) #polaczenie dwoch klas
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nazwa + " "
    #wyświetlanie nazw na głównej stronie


    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"

    
