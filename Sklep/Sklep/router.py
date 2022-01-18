from Produkty.viewsets import ProduktViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('produkt', ProduktViewset)
