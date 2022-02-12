from django import forms
from django.core import validators
from .models import NewModel
def check_for_h(value):
    if value[0].lower() != 'h':
        raise forms.ValidationError("Name needs to start with h")
class FormName(forms.ModelForm):
    name = forms.CharField(max_length=264,label='Enter name')#,validators=[check_for_h])
    email = forms.EmailField(max_length=264,label='Enter email')
    verify_email = forms.EmailField(max_length=264,label='Enter email again to verify')
    text = forms.CharField(widget=forms.Textarea)
    bot_check = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
    # To change the order of the fields in the form
    field_order = ["name","email","verify_email","text","bot_check"]
    class Meta:
        model = NewModel
        fields = ('name','email','text')

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError("EMAILS ARE NOT MATCHING")
