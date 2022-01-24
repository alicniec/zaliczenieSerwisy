from django.urls import path
from django.conf.urls import url, include

from .views import RegistrationAPIView, LoginAPIView 
#from .views import homeUser, RegisterView, LoginView

urlpatterns = [
    # url(r'^user/register/?$', RegistrationAPIView.as_view()),
    #url(r'^user/login/?$', LoginAPIView.as_view()),
    
    path('user/login/', LoginAPIView.as_view(), name='login'),
    path("user/register", RegistrationAPIView.as_view(), name="register"),
    # path("user/", homeUser, name="homeUser"),

    
]
