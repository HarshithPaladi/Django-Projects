from typing import Text
from django.http.response import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("HI FOOLS")
def get_subject(request,code):
    if code == 3:
        NAME = "Rakshit"
    else:
        NAME = "NO name BRUh"
    return TemplateResponse(request , "index.html",context = {"name" : NAME})