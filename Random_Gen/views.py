from django.shortcuts import render
import random
from django.http import HttpResponse
# Create your views here.
# Generate a sequence of random numbers with a given length n and maximum value m with no duplicates in the sequence and return the sequence as a csv file
def Random_gen(request):
    if request.method == 'GET':
        return render(request, 'rand_enter.html')
    if request.method == 'POST':
        n = int(request.POST['n'])
        m = int(request.POST['m'])
        if n > 0 and m > 0:
            if n > m:
                return render(request, 'Random_Gen.html', {'error': 'The number of elements in the sequence should be less than the maximum value',"n":n,"m":m})
            else:
                seq = []
                while len(seq) < n:
                    r = random.randint(1, m)
                    if r not in seq:
                        seq.append(r)
                seq.sort()
                return render(request, 'Random_Gen.html', {'seq': seq,"n":n,"m":m})
        else:
            return render(request, 'Random_Gen.html', {'error': 'The number of elements in the sequence should be greater than 0 and the maximum value should be greater than 0'})

    else:
        return HttpResponse('Invalid request')


# def Random_gen_fn(request):
#     # Get the number of random numbers to generate from the request.
#     n = int(request.GET.get('n', '10'))
#     # Get the maximum value from the request.
#     m = int(request.GET.get('m', '10'))
#     # Generate the random numbers.
#     rand_nums = [random.randint(0, m) for i in range(n)]
#     # Return the random numbers as a csv file.
#     return render(request, 'Random_Gen/Random_Gen.html', {'rand_nums': rand_nums})


# def Random_gen(request):
#     return render(request,"rand_enter.html")