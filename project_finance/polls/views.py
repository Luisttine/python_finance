from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'home/home.html')


# Category Actions
@csrf_exempt
def add_category(request):
    new_category = PurchaseCategory()
    new_category.category_name = request.POST.get('category_name')
    new_category.save()

    categories = {
        'category': PurchaseCategory.objects.all()
    }
    
    return render(request, 'category/list_categ.html', categories)

def category(request):
    return render(request, 'category/add_category.html')

def list_categ(request):
    
    categories = {
        'category': PurchaseCategory.objects.all()
    }
    return render(request, 'category/list_categ.html', categories)


# Bank Actions
@csrf_exempt
def add_bank(request):
    new_bank = Bank()
    new_bank.bank_name = request.POST.get('institution')
    new_bank.save()
    print(new_bank)

    banks = {
        'institution': Bank.objects.all()
    }
    
    return render(request, 'bank/list_bank.html', banks)

def bank(request):
    return render(request, 'bank/add_bank.html')

def list_bank(request):
    
    banks = {
        'institution': Bank.objects.all()
    }
    return render(request, 'bank/list_bank.html', banks)