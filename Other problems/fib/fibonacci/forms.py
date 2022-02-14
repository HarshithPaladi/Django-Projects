from django import forms


class fibform(forms.Form):
    numstr = forms.CharField(label="Enter a Value")
