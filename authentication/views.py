from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
# Create your views here.

class UsernameValdationView(View):
    def post(self,request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username error':'usearname should only contain alphanueric characters'},status=400)
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username error':'usearname is taken'},status=409)
        return JsonResponse({'username_valid':True})
        
class RegistrationView(View):
    def get(self,request):
        return render(request,'authentication/register.html')