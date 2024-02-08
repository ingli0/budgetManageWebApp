from django.shortcuts import render,redirect
from .models import Source,UserIncome
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from userpreferences.models import UserPrefence
# Create your views here.
       

@login_required(login_url='/authentication/login')
def index(request):
    categories=Source.objects.all()
    income = UserIncome.objects.filter(owner=request.user)

    paginator = Paginator(income,2)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator,page_number)
    curency=UserPrefence.objects.get(user=request.user).currency

    context={
        "income" : income,
        'page_obj':  page_obj,
        "Currancy" : curency
    }
    return render(request,'income/index.html',context)

@login_required(login_url='/authentication/login')
def add_income(request):
    sources = Source.objects.all()
    context={
            'sources':sources,
            'values':request.POST
        }
    if request.method == 'GET':
        
        return render(request,'income/add_income.html',context)

    if request.method =='POST':
        amount=request.POST['amount']

        if not amount :
            messages.error(request,'Amount is required')
            return render(request, 'income/add_income.html', context)
        
        
        date=request.POST['income_date']
        source=request.POST['source']
        description=request.POST['description']

        if not description :
            messages.error(request,'Description is required')
            return render(request, 'income/add_income.html', context)
        
        UserIncome.objects.create(owner=request.user, amount=amount,date=date,source=source,description=description)
        messages.success(request,'Income saved succesfully')

        return redirect('income')

        