from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . import models
from . import forms

# Create your views here.
def fibonac(nterms):
    # iterative method
    n1, n2 = 0, 1
    count = 0
    ls = []
    while count < nterms:
        ls.append(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
    return ls


def num(request):
    form = forms.fibform()
    if request.method == "POST":
        form = forms.fibform(request.POST)
        if form.is_valid():
            try:
                numstr = int(form.cleaned_data["numstr"])
                if numstr < 0:
                    return render(
                        request,
                        "num.html",
                        {
                            "form": form,
                            "msg": "Negetive value entered...Enter a positive number",
                        },
                    )
                else:
                    fib = fibonac(numstr)
                    fibstr = " ".join(str(x) for x in fib)
                    fibobj = models.Fibonacci(numstr=numstr, terms=fibstr)
                    fibobj.save()
                    return render(request, "num.html", {"form": form, "msg": fibstr})
            except:
                return render(
                    request,
                    "num.html",
                    {"form": form, "msg": "Text entered..Enter a number"},
                )
    return render(request, "num.html", {"form": form})


def fibo_archive(request):
    form = forms.fibform()
    fib_list = models.Fibonacci.objects.all()
    return render(request, "num.html", {"fib_list": fib_list, "form": form})
