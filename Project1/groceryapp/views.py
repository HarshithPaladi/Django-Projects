from django.shortcuts import render
from .models import Grocery
from .forms import GroceryForm
# Create your views here.
def grocery(request):
    custom_form = GroceryForm()
    if request.method == 'GET':
        return render(request, 'grocery.html', {'form': custom_form})
    elif request.method == 'POST':
        custom_form = GroceryForm(request.POST)
        if custom_form.is_valid():
            amount = custom_form.cleaned_data['quantity'] * custom_form.cleaned_data['price_peritem']
            test = Grocery.objects.get_or_create(name=custom_form.cleaned_data['name'], type=custom_form.cleaned_data['type'], quantity=custom_form.cleaned_data['quantity'], price_peritem=custom_form.cleaned_data['price_peritem'], total_price=amount)[0]
            test.save()
            return render(request, 'grocery.html', {'msg': 'Items Updated'})
        else:
            return render(request, 'grocery.html', {'error': 'Invalid Item Type'})
def view(request):
    items = Grocery.objects.all()
    return render(request, 'grocery.html', {'items': items})