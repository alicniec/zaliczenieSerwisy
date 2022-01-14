from xml.etree.ElementInclude import include
from django.urls import path
from django.conf.urls import url

from .views import RegistrationAPIView, UzytkownikViewSet

urlpatterns = [
    url(r'^user/register/?$', RegistrationAPIView.as_view()),
]
