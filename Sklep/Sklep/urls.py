"""Sklep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


import imp
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .router import router
from Uzytkownicy.views import *
from Produkty.viewsets import ProduktViewset
from django.conf import settings
from django.conf.urls.static import static
from Produkty.views import ProduktView
from Produkty.models import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProduktView.index),
    path('produkt/<id>', ProduktView.produkt, name='produkt'),
    path('kategoria/<id>', ProduktView.produkt, name='kategoria'),

    path('api/', include(router.urls)),
    
    path('api/', include('Uzytkownicy.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)