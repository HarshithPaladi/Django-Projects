from xml.dom.pulldom import parseString
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template.response import TemplateResponse
from .models import users, plist

def index(request):
    if request.method=="GET":
        #will display the login form
        return render(request,'login.html',{'flag': True})
    else:   
        username = request.POST['username']
        password = request.POST['password']
        username = users.objects.filter(username=username)
        '''
        if the username or password entered is not matching to the one
        we stored in the database then it will redirect to the login form
        and we have to fill the form again.
        '''
        if (not len(username)) or (username.first().password != password):
            return render(request,'login.html',{'flag': True})

        '''
        if the username and the password entered will match the username and password
        given in the database then it will redirect to the page where the price list
        and all will be displayed.
        '''
    return redirect('price/lol')
def price_list(request):
    if request.method=='GET':
        return render(request, "price_list.html",{'s':plist.objects.all()})
        

        
# Create your views here.
