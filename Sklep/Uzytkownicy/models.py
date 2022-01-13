from django.db import models
from django.contrib.auth.models import BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):

    # tworzenie użytkownika
    def create_user(self, username, email, password=None):
        user = None

        if username is None:
            raise TypeError("Users must have a username.")
        if email is None:
            raise TypeError("Users must have a email address.")
        
        user = Klient.objects.create(username = username, email = self.normalize_email(email))
        if user:
            user.set_password(password)
            user.save()
        
        return user


class Klient(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    
    username = models.CharField(db_index = True, max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    haslo = models.CharField(max_length=255)
    telefon = models.CharField(max_length=11)

    data_utworzenia = models.DateTimeField(auto_now_add=True, null=True)

    objects = UserManager()

    class Meta:
        verbose_name = "Klient"
        verbose_name_plural = "Klienci"
        ordering = ['username']
    
    def __str__(self):
        return self.username




