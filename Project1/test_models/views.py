from django.shortcuts import render
from .models import Topic,Webpage,AccessRecord
# Create your views here.
def test_models(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'test_models_in.html',context=date_dict)