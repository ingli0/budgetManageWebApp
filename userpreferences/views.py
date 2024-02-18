from django.shortcuts import render
import os 
import json
from django.conf import settings
from .models import UserPrefence
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='/authentication/login')
def index(request):
    currency_data=[]

    file_path = os.path.join(settings.BASE_DIR,'currencies.json')
        
    with open(file_path, 'r') as json_file:
        data=json.load(json_file)
        for k,v in data.items():
            currency_data.append({'name':k,'value':v})
    exists=UserPrefence.objects.filter(user=request.user).exists()
    User_Prefence=None
    
    if exists :
        User_Prefence=UserPrefence.objects.get(user=request.user)

    if request.method == 'GET':
            
        return render(request,'preferences/index.html',{'currencies':currency_data,'User_Prefence':User_Prefence})
    
    else:
        currency = request.POST["currency"]
        if exists:
            User_Prefence.currency = currency
            User_Prefence.save()
        else:
            UserPrefence.objects.create(user=request.user, currency=currency)
    messages.success(request, 'Changes saved')
    return render(request,'preferences/index.html',{'currencies':currency_data,'User_Prefence':User_Prefence})
