from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required(login_url='/authentication/login')
def index(request):
    return render(request,'managebudget/index.html')

def add_managebudget(request):
    return render(request,'managebudget/add_managebudget.html')
