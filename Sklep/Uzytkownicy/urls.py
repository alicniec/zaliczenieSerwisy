from xml.etree.ElementInclude import include
from django.urls import path
from django.conf.urls import url

from .views import RegistrationAPIView, UzytkownikViewSet, LoginAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    url(r'^user/register/?$', RegistrationAPIView.as_view()),
    url(r'^user/login/?$', LoginAPIView.as_view()),
]
