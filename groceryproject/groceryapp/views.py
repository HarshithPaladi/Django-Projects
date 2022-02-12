from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import models

# Create your views here.
def buy(request):
    form = forms.GroceryForm()
    if request.method == "GET":
        return render(request, "index.html", {"form": form})
    if request.method == "POST":
        form = forms.GroceryForm(request.POST)
        if form.is_valid():
            amt = form.cleaned_data["quantity"] * form.cleaned_data["rate_per_unit"]
            t = models.Grocery(
                name=form.cleaned_data["name"],
                type=form.cleaned_data["type"],
                quantity=form.cleaned_data["quantity"],
                rate_per_unit=form.cleaned_data["rate_per_unit"],
                amount=amt,
            )
            t.save()
        return HttpResponse("<h1>Thanks for buying</h1>")


def records(request):
    records = models.Grocery.objects.all()
    return render(request, "records.html", {"records": records})
