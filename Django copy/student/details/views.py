from unicodedata import name
from django.shortcuts import render
from distutils.log import error
import re
from django.shortcuts import render
from django.http import *
from django.template.response import TemplateResponse

def avg(m1, m2, m3):
    average = (m1+m2+m3)/3
    return average
def index(request):
    if request.method == "GET":
        return TemplateResponse(request, "index.html" , context = {})
    try:

        if request.method == "POST":
            n = str(request.POST.get("fname",None))
            x = str(request.POST.get("lname",None))
            a = int(request.POST.get("year",None))
            b = int(request.POST.get("mark 1",None))
            c = int(request.POST.get("mark 2",None))
            d = int(request.POST.get("mark 3",None))
            e = float(avg(b,c,d))
            return TemplateResponse(request , "response.html" , context ={"n" :n , "x" :x, "a" :a, "b": b, "c" : c, "d" :d, "e": e})

    except Exception as e:
        return HttpResponse("error occurred!!")

# Create your views here.
