from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
    if request.method == 'GET':
        return render(request, 'test.html')
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        m = int(request.POST.get('m'))
        if n > m:
            return render(request, 'out.html', {'n': n, 'm': m})
        else:
            return HttpResponse("<h1>Input Error Occurred!<h1><h2>Error Message: <h2>%s must be greater than %s" % (n, m))