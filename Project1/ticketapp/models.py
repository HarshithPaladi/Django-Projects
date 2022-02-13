from django.db import models
ch =[('Mumbai','Mumbai'),('Delhi','Delhi'),('Kolkata','Kolkata'),('Hyderabad','Hyderabad'),('Chennai','Chennai'),('Bangalore','Bangalore')]
# Create your models here.
class BusDetails(models.Model):
    bus_no = models.IntegerField(primary_key=True)
    Departure_time = models.TimeField()
    Destinations = models.CharField(max_length=50,choices=ch,default='Hyderabad')
    available_seats = models.IntegerField()
    Ticket_cost = models.IntegerField()
    def __str__(self):
        return self.Destinations