from django import forms
from .models import Grocery
class GroceryForm(forms.ModelForm):
    class Meta:
        model = Grocery
        fields = ['name', 'type', 'quantity', 'price_peritem']