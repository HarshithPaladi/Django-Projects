from django.shortcuts import render
from .models import Topic, User,Webpage,AccessRecord
# Create your views here.
def test_models(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'test_models_in.html',context=date_dict)
def test_users(request):
    data = User.objects.order_by('first_name')
    user_dict = {'users':data}
    return render(request,'test_users.html',context=user_dict)