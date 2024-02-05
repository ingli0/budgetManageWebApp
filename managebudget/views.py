from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Category,Expense
# Create your views here.


@login_required(login_url='/authentication/login')
def index(request):
    categories=Category.objects.all()
    return render(request,'managebudget/index.html')

def add_managebudget(request):
    categories=Category.objects.all()
    context={
        'categories':categories
    }
    return render(request,'managebudget/add_managebudget.html',context)
