from django.shortcuts import render

# Create your views here.
import math

def divisorGenerator(n):
    # lst = []
    # i = 2
    # while i <= math.sqrt(n):
    #     if n%1 == 0:
    #         if i == (n/i):
    #             lst.append(i)
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield int(divisor)
    
def perfect_num(request):
    if request.method == "GET":
        return render(request, "perfect_num_in.html")
    try:
        if request.method == "POST":
            n = int(request.POST["n"])
            lst = list(divisorGenerator(n))
            lst.remove(n)
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
                lst = list(divisorGenerator(i))
                lst.remove(i)
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
