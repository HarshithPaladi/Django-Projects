from django.shortcuts import render
from .graph import Graph, g
# Create your views here.
def printGraph(request):
    return render(request, 'index.html', {'e_list':g.sortEdges()})
def printLists(request):
    alist, dlist, elist =  check_property(30)
    return render(request, 'property.html', {'a_list':alist, 'dlist':dlist, 'elist':elist})
def checkAmicable(request):
    pairs = [(150, 290), (220, 284), (1184, 1210), (1350, 1851)]
    dpairs = {}
    for x,y in pairs:
        dpairs[(x,y)] = isAmicable_pair(x, y)
    return render(request, 'amicable.html', {'pairs':dpairs.items()})
def get_proper_divisors(N):
    divisors = [x for x in range(1, N) if N % x == 0]
    return divisors
def check_property(N):
    abundant_list = [x for x in range(2, N+1) if sum(get_proper_divisors(x)) > x]
    deficient_list = [x for x in range(2, N+1) if sum(get_proper_divisors(x)) < x]
    equal_list = [x for x in range(2, N+1) if sum(get_proper_divisors(x)) == x]
    return abundant_list, deficient_list, equal_list

def isAmicable_pair(x, y):
    div_x = get_proper_divisors(x)
    div_y = get_proper_divisors(y)
    sum_div_x = sum(div_x)
    sum_div_y = sum(div_y)
    if sum_div_x == y and sum_div_y == x:
        return "AMICABLE"
    else:
        return "NOT AMICABLE"
