# from django.contrib.auth import get_user_model
# from django.contrib.auth.backends import ModelBackend

from sys import prefix
import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from .models import Uzytkownik

# class CaseInsensitiveModelBackend(ModelBackend):

#     def authenticate(self, request, username=None, password=None, **kwargs):
#         UserModel = get_user_model()

#         if username is None:
#             username = kwargs.get(UserModel.USERNAME_FIELD)

#         try:
#             case_insensitive_username_filed = '{}__iexact'.format(UserModel.USERNAME_FIELD)
#             user = UserModel._default_manager.get(**{case_insensitive_username_filed: username})
#         except UserModel.DoesNotExist:
#             UserModel().set_password(password)

#         else:
#             if user.check_password(password) and self.user_can_authenticate(user):
#                 return user

class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = "token"

    def authenticate(self, request):

        request.user = None

        auth_header = authentication.get_authorization_header(request).split()
        print(auth_header)
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None

        if len(auth_header) == 1:
            raise exceptions.AuthenticationFailed("Invalid token header.")
        elif len(auth_header) > 2:
            raise exceptions.AuthenticationFailed("Invalid token header.")
        
        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix.lower() != auth_header_prefix:
            #Auth header prefix is not what expected
            return None
        
        return self.authenticate_credentials(request, token)

    def authenticate_credentials(self, request, token):
        payload= {}
        try: 
            print(token)
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except Exception as e: #InvalidSignatureError
            print(str(e))

            #raise exceptions.AuthenticationFailed("Autentykcja nie powiodła się. Nie można odkodować tokenu.")
        
        
        user = None

        try:
            user = Uzytkownik.objects.get(pk=payload['id'])
        except Uzytkownik.DoesNotExist:
            raise exceptions.AuthenticationFailed("Nie znaleziono użytkownika!")
        
        if not user.is_active:
            raise exceptions.AuthenticationFailed("To konto jest nieaktywne.")
        
        return user, token
    
    

