from django.shortcuts import render
from .forms import Ticket
from .models import *
# Create your views here.
def ticket(request):
    custom_form = Ticket()
    if request.method == 'GET':
        return render(request, 'ticket_in.html', {'form': custom_form})
    elif request.method == 'POST':
        custom_form = Ticket(request.POST)
        if custom_form.is_valid():
            bus_no = custom_form.cleaned_data['bus_no']
            no_of_persons = custom_form.cleaned_data['No_of_persons']
            destination = custom_form.cleaned_data['destination']
            s = BusDetails.objects.filter(bus_no=bus_no)
            
            if s.exists():
                sa = BusDetails.objects.get(bus_no=bus_no)
                if sa.Destinations == destination:
                    if sa.available_seats >= no_of_persons:
                        sa.available_seats = sa.available_seats - no_of_persons
                        sa.save()
                        cost = sa.Ticket_cost * no_of_persons
                        
                        custom_form.clean()
                        return render(request, 'ticket_in.html', {'msg': 'Booking Successful', 'cost': cost})
                    else:
                        return render(request, 'ticket_in.html', {'error': 'No seats available'})
                else:
                    return render(request, 'ticket_in.html', {'error': 'Invalid Destination'})
            else:
                return render(request, 'ticket_in.html', {'error': 'Invalid Bus Number'})
    return render(request, 'ticket_in.html', {'form': custom_form})