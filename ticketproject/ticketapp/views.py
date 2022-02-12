from django import forms
from django.shortcuts import render
from . import forms
from . import models

# Create your views here.
def bookticket(request):
    form = forms.BookTicket()
    if request.method == "POST":
        form = forms.BookTicket(request.POST)
        if form.is_valid():
            bus_no = form.cleaned_data["bus_no"]
            no_of_persons = form.cleaned_data["no_of_persons"]
            sa = models.BusDetails.objects.filter(bus_no=bus_no)

            if sa.exists():
                s = models.BusDetails.objects.get(bus_no=bus_no)
                if s.destination == form.cleaned_data["destination"]:
                    if s.seats_available >= no_of_persons:
                        s.seats_available = s.seats_available - no_of_persons
                        s.save()
                        cost = no_of_persons * s.ticket_cost
                        return render(
                            request,
                            "bookticket.html",
                            {
                                "error": "Booked successfully",
                                "cost": cost,
                                "form": forms.BookTicket(),
                            },
                        )
                    else:
                        return render(
                            request,
                            "bookticket.html",
                            {
                                "error": "No seats available",
                                "form": forms.BookTicket(),
                            },
                        )
                else:
                    return render(
                        request,
                        "bookticket.html",
                        {
                            "form": form,
                            "error": "Wrong destination",
                        },
                    )
            else:
                return render(
                    request,
                    "bookticket.html",
                    {
                        "form": form,
                        "error": "Invalid busnumber",
                    },
                )
    return render(request, "bookticket.html", {"form": form})
