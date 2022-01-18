from Produkty.viewsets import ProduktViewset, KategoriaViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('produkt', ProduktViewset, KategoriaViewset)
