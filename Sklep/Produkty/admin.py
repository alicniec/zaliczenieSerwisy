from django.contrib import admin
from .models import Produkty, Gatunki, Kategoria

# Register your models here.


admin.site.register(Produkty) #Dodanie produktów do konsoli admina na web stronnie
admin.site.register(Gatunki)
admin.site.register(Kategoria)
