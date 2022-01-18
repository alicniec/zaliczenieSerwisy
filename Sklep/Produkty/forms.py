from django import forms
from .models import *
  
class ProduktForm(forms.ModelForm):
  
    class Meta:
        model = Produkt
        fields = '__all__'