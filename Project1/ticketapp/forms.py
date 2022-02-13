from django import forms
ch = [('Mumbai','Mumbai'),('Delhi','Delhi'),('Kolkata','Kolkata'),('Hyderabad','Hyderabad'),('Chennai','Chennai'),('Bangalore','Bangalore')]
class Ticket(forms.Form):
    bus_no = forms.IntegerField(label='Bus No.',max_value=10)
    destination = forms.ChoiceField(choices=ch,label='Destination')
    No_of_persons = forms.IntegerField(label='No. of Persons',min_value=1,max_value=10)
