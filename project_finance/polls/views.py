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
    print(new_category, ' was successfuly added.')

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

    print(categories)
    return render(request, 'category/list_categ.html', categories)


# Bank Actions
@csrf_exempt
def add_bank(request):
    new_bank = Bank()
    new_bank.institution = request.POST.get('institution')
    new_bank.save()
    print(new_bank, ' was successfuly added.')

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

    print(banks)
    return render(request, 'bank/list_bank.html', banks)


# Purchase Actions
@csrf_exempt
def add_purchase(request):
    new_purchase = Purchase()
    new_purchase.product = request.POST.get('product')
    new_purchase.purchase_category = request.POST.get('category')
    new_purchase.payment_type = request.POST.get('pay_type')
    new_purchase.total_value = request.POST.get('total')
    new_purchase.purchase_date = request.POST.get('purchase_date')

    new_purchase.save()
    print(new_purchase, ' was successfuly added.')

    purchases = {
        'product': Purchase.objects.all()
    }
    
    return render(request, 'purchase/list_purchase.html', purchases)

def purchase(request):
    banks = {
        'institution': Bank.objects.all()
    }

    categories = {
    'category': PurchaseCategory.objects.all()
    }

    return render(request, 'purchase/add_purchase.html', {'banks': banks, 'categories': categories  })

def list_purchase(request):
    
    purchases = {
        'product': Purchase.objects.all()
    }

    print(purchases)
    return render(request, 'purchase/list_purchase.html', purchases)