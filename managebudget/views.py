from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Category,Expense
# Create your views here.
from django.contrib import messages 


@login_required(login_url='/authentication/login')
def index(request):
    categories=Category.objects.all()
    return render(request,'managebudget/index.html')

def add_managebudget(request):
    categories = Category.objects.all()
    context={
            'categories':categories
        }
    if request.method == 'GET':
        
        return render(request,'managebudget/add_managebudget.html',context)

    if request.method =='POST':
        amount=request.POST['amount']

        if not amount :
            messages.error(request,'Amount is required')
            return render(request, 'managebudget/add_managebudget.html', context)

        
     