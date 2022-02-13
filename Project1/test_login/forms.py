from django import forms
from .models import Form1
class InputForm(forms.ModelForm):
    class Meta:
        model = Form1
        fields = ['name', 'email', 'age']