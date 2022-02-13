from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, User,Webpage,AccessRecord
from .forms import *
# Create your views here.
def test_models(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'test_models_in.html',context=date_dict)
def test_users(request):
    data = User.objects.order_by('first_name')
    user_dict = {'users':data}
    return render(request,'test_users.html',context=user_dict)
def test_forms(request):
    form_custom = FormName()
    if request.method == 'GET':
        return render(request,'test_forms_in.html',{'form':form_custom})
    if request.method == 'POST':
        form_custom = FormName(request.POST)
        if form_custom.is_valid():
            print("Validation Successful")
            print("Name: "+form_custom.cleaned_data['name'])
            print("Email: "+form_custom.cleaned_data['email'])
            print("Text: "+form_custom.cleaned_data['text'])
            form_custom.save(commit=True)
            form_custom.clean()
            #return test_forms(request)
            return render(request,'test_forms_out.html',{'form':form_custom})
            #return HttpResponse("<h1>Form Submitted Successfully <h2><a href="" {% url 'test_forms' %}> To Fill another form Click here</a></h2></h1>")
        
        else:
            print("Validation Failed")
    #return render(request,'test_forms_in.html',{'form':form_custom})