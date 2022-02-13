from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Form1
class InputForm(forms.ModelForm):
    class Meta:
        model = Form1
        fields = ['name', 'email', 'age']