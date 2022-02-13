from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render

from .forms import *
from .models import *
# Create your views here.
@login_required
def forms(request):
    if request.user.is_authenticated:
        custom_form = InputForm()
        if request.method == 'GET':
            return render(request,'form1_in.html',{'form':custom_form})
        if request.method == 'POST':
            custom_form = InputForm(request.POST)
            if custom_form.is_valid():
                print("Validation Successful")
                print("Name: "+custom_form.cleaned_data['name'])
                print("Email: "+custom_form.cleaned_data['email'])
                print("Age: "+str(custom_form.cleaned_data['age']))
                custom_form.save(commit=True)
                custom_form.clean()
                return render(request,'form1_out.html',{'form':custom_form})
            
            else:
                print("Validation Failed")
                return render(request,'form1_in.html',{'error':'Invalid Input','form':custom_form})
    else:
        print("Please Login First")
        return render(request,'form1_in.html',{'error':'Please Login First'})
@login_required
def forms_data(request):
    data = Form1.objects.order_by('name')
    return render(request,'form1_out.html',{'data':data})
    