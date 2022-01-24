from django.db import models
from Produkty.models import Produkt
from Uzytkownicy.models import Uzytkownik
# Create your models here.


class Item(models.Model):
    product = models.OneToOneField(Produkt, on_delete=models.SET_NULL, null = True)
    is_added = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.nazwa


class ItemsCart(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Uzytkownik, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(Item)

    def get_cart_items(self):
        return self.items.all()

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)
