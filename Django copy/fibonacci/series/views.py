from distutils.log import error
import re
from django.shortcuts import render
from django.http import *
from django.template.response import TemplateResponse

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return "0 1"
    a = 0
    b = 1
    x = "0 1 "
    while(n-2):
        c=a+b
        a,b = b,c
        x = x + str(c) + " "
        n=n-1
    return x

def index(request):
    if request.method == "GET":
        return TemplateResponse(request, "index.html" , context = {})
    try:

        if request.method == "POST":
            n = request.POST.get("value", None)
            n = int(n)
            x = fib(n)
            return TemplateResponse(request , "series.html" , context ={ "x" : x , "n" :n})

    except Exception as e:
        return HttpResponse("error occurred!!")
    
