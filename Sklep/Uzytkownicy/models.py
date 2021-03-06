from sqlite3 import connect
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

import jwt
import datetime
from django.conf import settings
from django.core.mail import send_mail

# Create your models here.

class UserManager(BaseUserManager):

    # tworzenie użytkownika
    def create_user(self, username, email, haslo=None):
        user = None

        if username is None:
            raise ValueError("Users must have a username.")
        if email is None:
            raise ValueError("Users must have a email address.")
        
        user = Uzytkownik.objects.create(username = username, email = self.normalize_email(email))
        if user:
            user.set_password(haslo)
            user.save()

        send_mail(
            'Rejestracja konta',
            'Cześć ' + username + '! Twoje konto w serwisie zostało utworzone.',
            'sklepkwiatki@gmail.com',
            [email],
        )

        return user

    def create_superuser(self, username, email, haslo):
        if haslo is None:
            raise ValueError('Superusers must have a password')
        
        user = self.create_user(username, email, haslo)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class Uzytkownik(AbstractBaseUser):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    
    username = models.CharField(db_index = True, max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    haslo = models.CharField(max_length=255)
    telefon = models.CharField(max_length=11)

    data_utworzenia = models.DateTimeField(auto_now_add=True, null=True)

    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "Użytkownik"
        verbose_name_plural = "Użytkownicy"
        ordering = ['username']
    
    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

    @property
    def token(self):
        return self._generate_jwt_token()
    
    def _generate_jwt_token(self):
        exp = datetime.datetime.now() + datetime.timedelta(days=60)
        iat = datetime.datetime.now()

        payload = {
            'id': self.id,
            'exp': datetime.datetime.now() + datetime.timedelta(days=60), #czas działa tokenu
            'iat': datetime.datetime.now() #kiedy token został wygenerowany
        }

        token = jwt.encode(payload, "SECRET_KEY", algorithm='HS256')

        return token



