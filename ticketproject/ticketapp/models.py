from django.db import models

ch = [
    ("Thanjavur", "Thanjavur"),
    ("chennai", "chennai"),
    ("Madurai", "Madurai"),
    ("Coimbatore", "Coimbatore"),
    ("erode", "erode"),
    ("ooty", "ooty"),
    ("bcm", "bcm"),
]
# Create your models here.
class BusDetails(models.Model):
    bus_no = models.CharField(max_length=10)
    departure_time = models.TimeField()
    destination = models.CharField(max_length=20, choices=ch, default="Thanjavur")
    seats_available = models.IntegerField()
    ticket_cost = models.IntegerField()

    def __str__(self):
        return self.destination
