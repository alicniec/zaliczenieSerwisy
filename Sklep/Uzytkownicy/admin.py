from csv import list_dialects
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Uzytkownicy.models import Uzytkownik

# Register your models here.


class KontoAdmina(UserAdmin):
    list_display = ('email', 'username', 'data_utworzenia', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'data_utworzenia')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Uzytkownik, KontoAdmina)


#admin.site.register(Uzytkownik)