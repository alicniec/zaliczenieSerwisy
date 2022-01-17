from django.urls import path
from django.conf.urls import url, include

from .views import RegistrationAPIView, LoginAPIView
#from .views import homeUser, RegisterView, LoginView

urlpatterns = [
    url(r'^user/register/?$', RegistrationAPIView.as_view()),
    url(r'^user/login/?$', LoginAPIView.as_view()),
    # path("user/", homeUser, name="homeUser"),
    # path("user/register", RegisterView, name="rejestracja"),
    # path("user/login", LoginView, name="logowanie"),
    
]
