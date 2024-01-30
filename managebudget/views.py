from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'managebudget/index.html')

def add_managebudget(request):
    return render(request,'managebudget/add_managebudget.html')
