from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# def divisorGenerator(n):
#     large_divisors = []
#     for i in range(1, int(math.sqrt(n) + 1)):
#         if n % i == 0:
#             yield i
#             if i*i != n:
#                 large_divisors.append(n / i)
#     for divisor in reversed(large_divisors):
#         yield int(divisor)
def divisorGenerator(n):
    Lst = [x for x in range(1, n) if n % x == 0]
    return Lst
    
def perfect_num(request):
    if request.method == "GET":
        return render(request, "perfect_num_in.html")
    try:
        if request.method == "POST":
            n = int(request.POST["n"])
            lst = divisorGenerator(n)
            #lst.remove(n)
            return render(request, "perfect_num_out.html", {"lst": lst,"n":n})
        
    except Exception as f:
        return render(
            request,
            "perfect_num_out.html",
            {
                "error": f,
            },
        )
def choose(request):
    return render(request, "choose.html")
def num_stats(request):
    if request.method == "GET":
        return render(request, "num_stats_in.html")
    try:
        if request.method == "POST":
            perfect_num = []
            deficient_num = []
            abundant_num = []
            n1 = int(request.POST["n1"])
            n2 = int(request.POST["n2"])
            for i  in range(n1,n2+1):
                lst = divisorGenerator(i)
                #lst.remove(i)
                if sum(lst) == i:
                    perfect_num.append(i)
                if sum(lst) < i:
                    deficient_num.append(i)
                if sum(lst) > i:
                    abundant_num.append(i)
            return render(request, "num_stats_out.html", {"perfect_num": perfect_num, "deficient_num": deficient_num, "abundant_num": abundant_num, "n1": n1, "n2": n2})
    except Exception as f:
        return render(
            request,
            "num_stats_out.html",
            {
                "error": f,
            },
        )
def amicable(request):
    if request.method == "GET":
        return render(request, "num_stats_in.html")
    try:
        if request.method == "POST":
            n1 = int(request.POST["n1"])
            n2 = int(request.POST["n2"])
            return HttpResponse("<h1>{}</h1>".format(check_amicable(n1,n2,True)))
    except Exception as f:
        return render(
            request,
            "num_stats_out.html",
            {
                "error": f,
            },
        )

def check_amicable(n1,n2,x=False):
    sum1 = sum(divisorGenerator(n1))
    sum2 = sum(divisorGenerator(n2))
    if x == True:
        if sum1 == n2 and sum2 == n1:
            return f"{n1} and {n2} are amicable"
        else:
            return f"{n1} and {n2} are not amicable"
    else:
        if sum1 == n2 and sum2 == n1:
            return "Amicable"
        else:
            return "Not Amicable"

def static_amicable(request):
    if request.method == "GET":
        dpairs = {}
        pairs = [(150, 290), (220, 284), (1184, 1210), (1350, 1851)]
        for x,y in pairs:
            dpairs[(x,y)] = check_amicable(x,y)
        return render(request, "static_amicable.html", {"pairs": dpairs.items()})
            



