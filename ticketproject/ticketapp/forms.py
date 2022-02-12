from django import forms

ch = [
    ("Thanjavur", "Thanjavur"),
    ("chennai", "chennai"),
    ("Madurai", "Madurai"),
    ("Coimbatore", "Coimbatore"),
    ("erode", "erode"),
    ("ooty", "ooty"),
    ("bcm", "bcm"),
]


class BookTicket(forms.Form):
    bus_no = forms.CharField(max_length=10)
    destination = forms.ChoiceField(choices=ch)
    no_of_persons = forms.IntegerField()
