from django.shortcuts import render
import random
from django.http import HttpResponse
# Create your views here.
# Generate a sequence of random numbers with a given length n and maximum value m with no duplicates in the sequence and return the sequence as a csv file
def Random_gen(request):
    # TODO: Return the sequence of random numbers as a csv file
    if request.method == 'GET':
        return render(request, 'rand_enter.html')
    try:
        if request.method == 'POST':
            n = int(request.POST['n'])
            m = int(request.POST['m'])
            if n > 0 and m > 0:
                # if n > m:
                #     return render(request, 'Random_Gen.html', {'error': 'The number of elements in the sequence should be less than the maximum value',"n":n,"m":m})
                seq = []
                while len(seq) < n-1:
                    r = random.randint(-m, m-1) # Generate a random number between -m and m-1 so that the number is not in the sequence
                    if r not in seq:
                        seq.append(r)
                seq.insert(random.randint(0,n-1),m) # Appending the maximum value to the sequence at a index randomly chosen
                #random.shuffle(seq) # Shuffling the sequence # Depreceated due to better optimized solution found
                #seq.sort()
                lst = [str(i) for i in seq]
                res = render(request, 'Random_Gen.html', {'lst': ','.join(lst)})
                with open("Random_Gen/Random_Sequence.csv", "w") as f:
                    f.write(','.join(lst))
                #return res
                # Convert the sequence to a string and return it
                # return HttpResponse(','.join(lst))  
                return res


                

                # return render(request, 'Random_Gen.html', {'seq': seq,"n":n,"m":m})
            else:
                return render(request, 'Random_Gen.html', {'error': 'The number of elements in the sequence should be greater than 0 and the maximum value should be greater than 0',"n":n,"m":m})

        else:
            return HttpResponse('Invalid request 404/666 <br> <a href="/">Go back to home page</a>')
    except Exception as f:
        return HttpResponse('<h1>Error: </h1>' + str(f))

def Random_csv(request):
    if request.method == 'GET':
        with open("Random_Gen/Random_Sequence.csv", "r") as myfile:
            response = HttpResponse(myfile,content_type='text/csv')
            filename="Random_Sequence.csv"
            response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
            return response
    else:
        return HttpResponse('Invalid request 404/666 <br> <a href="/">Go back to home page</a>')

