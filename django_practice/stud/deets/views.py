from lib2to3.pgen2.token import NUMBER

import string
from tokenize import Number
from django.shortcuts import render
from unicodedata import name
from django.shortcuts import render,redirect
from distutils.log import error
import re
from django.shortcuts import render
from django.http import *
from django.template.response import TemplateResponse
from .models import *


    

def index(request):
     var=None
     if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        item = users.objects.filter(username=username)
        if (not len(item)) or (item.first().password != password):
            return render(request,'login.html',{'flag': True})
        
    
        return redirect('results/grade')
        

     return render(request,'login.html',{'flag': False})

def results(request):
    if request.POST:
        name = request.POST['name']
        reg_no = request.POST['reg']
        m1 = int(request.POST['m1'])
        m2 = int(request.POST['m2'])
        m3 = int(request.POST['m3'])
        (g1, g2, g3) = [grade_calc(x) for x in [m1, m2, m3]]
        stud_record.objects.create(name=name,register_no = reg_no,mark_1 = m1,grade_1=g1, mark_2 = m2,grade_2=g2,mark_3 = m3,grade_3=g3)

        return render(request, 'output.html', {'records':stud_record.objects.all()})

        
    return render(request, 'marks.html')

def grade_calc(m):
    if m > 90:
        return 'S'
    elif m > 85:
        return 'X'
    elif m > 75:
        return 'A'
    elif m > 65:
        return 'B'
    elif m > 55:
        return 'D'
    elif m > 50:
        return 'D'
    else:
        return 'F'

# Create your views here.
