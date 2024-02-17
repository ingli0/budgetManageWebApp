from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Category,Expense
# Create your views here.
from django.contrib import messages 
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import json
from userpreferences.models import UserPrefence
from django.http import JsonResponse,HttpResponse
import datetime
import csv
from collections import defaultdict
import xlwt


def search_expenses(request):
    if request.method == 'POST':

        search_str = json.loads(request.body).get('searchText')
        expenses = Expense.objects.filter(
            amount__istartswith =search_str,owner=request.user) | Expense.objects.filter(
            date__istartswith =search_str,owner=request.user) |   Expense.objects.filter(
            description__icontains=search_str,owner=request.user) | Expense.objects.filter(
            category__istartswith=search_str,owner=request.user)
        
        data= expenses.values()
        return JsonResponse(list(data),safe=False)
        

@login_required(login_url='/authentication/login')
def index(request):
    categories=Category.objects.all()
    expenses = Expense.objects.filter(owner=request.user)

    paginator = Paginator(expenses,2)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator,page_number)
    curency=UserPrefence.objects.get(user=request.user).currency

    context={
        "expenses" : expenses,
        'page_obj':  page_obj,
        "Currancy" : curency
    }
    return render(request,'managebudget/index.html',context)

@login_required(login_url='/authentication/login')
def add_managebudget(request):
    categories = Category.objects.all()
    context={
            'categories':categories,
            'values':request.POST
        }
    if request.method == 'GET':
        
        return render(request,'managebudget/add_managebudget.html',context)

    if request.method =='POST':
        amount=request.POST['amount']

        if not amount :
            messages.error(request,'Amount is required')
            return render(request, 'managebudget/add_managebudget.html', context)
        
        
        date=request.POST['expense_date']
        category=request.POST['category']
        description=request.POST['description']

        if not description :
            messages.error(request,'Description is required')
            return render(request, 'managebudget/add_managebudget.html', context)
        
        Expense.objects.create(owner=request.user, amount=amount,date=date,category=category,description=description)
        messages.success(request,'Expense saved succesfully')

        return redirect('managebudget')

        
def expense_edit(request,id):
    expense = Expense.objects.get(pk=id)
    categories=Category.objects.all()

    context = {
        'expense':expense,
        'values':expense,
        'categories':categories
    }
    if request.method=='GET':
        return render(request,'managebudget/edit-expense.html',context)
    
    if request.method=='POST':
        amount=request.POST['amount']

        if not amount :
            messages.error(request,'Amount is required')
            return render(request, 'managebudget/edit-expense.html', context)
        
        
        date=request.POST['expense_date']
        category=request.POST['category']
        description=request.POST['description']

        if not description :
            messages.error(request,'Description is required')
            return render(request, 'managebudget/edit-expense.html', context)
        
        expense.owner=request.user
        expense.amount=amount
        expense.date=date
        expense.category=category
        expense.description=description

        expense.save()
        messages.success(request,'Expense Updated succesfully')

        return redirect('managebudget')
    
def delete_expense(request,id):
    expense = Expense.objects.get(pk=id)
    expense.delete()
    messages.success(request,'Expense removed')
    return redirect('managebudget')


def expense_category_summary(request):
    expenses = Expense.objects.filter(owner=request.user)

    finalrep = {}

    for expense in expenses:
        if expense.category not in finalrep:
            finalrep[expense.category] = 0
        finalrep[expense.category] += expense.amount

    return JsonResponse({'expense_category_data': finalrep})


def statsView(request):
    return render(request,'managebudget/stats.html')


def export_csv(request):
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=Expenses'+\
       str( datetime.datetime.now())+'.csv'
    
    writer = csv.writer(response)
    writer.writerow(['Amount','Description','Category','Date'])

    expenses=Expense.objects.filter(owner=request.user)

    for expense in expenses:
        writer.writerow([expense.amount,expense.description,expense.category,expense.date])

    return response


def export_excel(request):
    response=HttpResponse(content_type='application/ms-excel')

    response['Content-Disposition']='attachment; filename=Expenses'+\
       str( datetime.datetime.now())+'.xls'
    
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Expenses')
    row_num=0
    font_style = xlwt.XFStyle()
    font_style.font.bold= True
    columns=['Amount','Description','Category','Date']

    for col_num in range (len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style = xlwt.XFStyle()

    rows =Expense.objects.filter(owner=request.user).values_list('amount','description','category','date')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    wb.save(response)

    return response