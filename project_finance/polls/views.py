from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages 

def home(request):
    return render(request, 'home/home.html')


# Category Actions
@csrf_exempt
def add_category(request):
    if PurchaseCategory.objects.filter(category_name=request.POST.get('category_name')):
        messages.error(request, f"({request.POST.get('category_name')}) already exists! Try another category name.")
    else:
        new_category = PurchaseCategory()
        new_category.category_name = request.POST.get('category_name')
        new_category.save()

        print(new_category, 'was successfuly added.')
        messages.success(request, f"({new_category}) was successfuly added.")

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

    if not categories:
        print('There are no categories yet! Try register a new one by clicking ')

    print(categories)
    return render(request, 'category/list_categ.html', categories)

def delete_categ(request, category_id):
    if PurchaseCategory.objects.filter(id_purchase_category=category_id):
        categ = get_object_or_404(PurchaseCategory, id_purchase_category=category_id)
        categ.delete()

        print(f'{categ} excluido com sucesso!')
        messages.success(request, f"({categ}) was deleted successfuly.")
    else:
        messages.error(request, f"{category_id} does not exists.")
        print(f'{category_id} does not exist!')

    response = redirect('/list_categ')
    return response

@csrf_exempt
def edit_categ(request, category_id):
    categ = get_object_or_404(PurchaseCategory, id_purchase_category=category_id)

    if request.method == 'POST':
        categ.category_name = request.POST.get('category_name')
        categ.save()
        return redirect('list_categ')  # Redireciona para a página de listagem de categorias

    return render(request, 'category/edit_category.html', {"categ": categ})


# Bank Actions
@csrf_exempt
def add_bank(request):
    if Bank.objects.filter(institution=request.POST.get('institution')):
        messages.error(request, f"({request.POST.get('institution')}) already exists! Try another institution name.")
    else:
        new_bank = Bank()
        new_bank.institution = request.POST.get('institution')
        new_bank.save()

        print(new_bank, 'was successfuly added.')
        messages.success(request, f"({new_bank}) was successfuly added.")

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

    if not banks:
        print('There are no institutions yet! Try register a new one by clicking ')
        
    print(banks)
    return render(request, 'bank/list_bank.html', banks)

def delete_bank(request, bank_id):
    if Bank.objects.filter(id_bank=bank_id):
        categ = get_object_or_404(Bank, id_bank=bank_id)
        categ.delete()

        print(f'{categ} excluido com sucesso!')
        messages.success(request, f"({categ}) was deleted successfuly.")
    else:
        messages.error(request, f"{bank_id} does not exists.")
        print(f'{bank_id} does not exist!')

    response = redirect('/list_bank')
    return response

@csrf_exempt
def edit_bank(request, bank_id):
    bank = get_object_or_404(Bank, id_bank=bank_id)

    if request.method == 'POST':
        bank.institution = request.POST.get('institution')
        bank.save()
        return redirect('list_bank')  # Redireciona para a página de listagem de banks

    return render(request, 'bank/edit_bank.html', {"bank": bank})

# Purchase Actions
@csrf_exempt
def add_purchase(request):
    if Purchase.objects.filter(product=request.POST.get('product')):
        messages.error(request, f"({request.POST.get('product')}) already exists! Try another product name.")
    else:
        new_purchase = Purchase()
        new_purchase.product = request.POST.get('product')
        new_purchase.purchase_category = PurchaseCategory.objects.get(pk=request.POST.get('category_id'))
        new_purchase.bank =  Bank.objects.get(pk=request.POST.get('bank_id'))
        new_purchase.payment_type = request.POST.get('payment_type')
        new_purchase.total_value = request.POST.get('total')
        new_purchase.purchase_date = request.POST.get('purchase_date')
        new_purchase.save()

        print(new_purchase.product, 'was successfuly added.')
        messages.success(request, f"({new_purchase.product}) was successfuly added.")

    response = redirect('/list_purchase')

    return response

def purchase(request):
    banks = {
        'institution': Bank.objects.all()
    }

    categories = {
    'category': PurchaseCategory.objects.all()
    }

    #print(banks)
    return render(request, 'purchase/add_purchase.html', {"banks" : banks,  "categories" : categories   })

def list_purchase(request):
    
    purchases = {
        'purchase': Purchase.objects.all()
    }

    if not purchases:
        print('There are no purchases yet! Try register a new one by clicking ')
        
    print(purchases)
    return render(request, 'purchase/list_purchase.html', purchases)

def delete_purchase(request, purchase_id):
    if Purchase.objects.filter(id_purchase=purchase_id):
        pur = get_object_or_404(Purchase, id_purchase=purchase_id)
        pur.delete()
        print(f'Product {pur.product} excluido com sucesso!')
        messages.success(request, f"({pur.product}) was deleted successfuly.")
    else:
        messages.error(request, f"{purchase_id} does not exists.")
        print(f'{purchase_id} does not exist!')

    response = redirect('/list_purchase')
    return response

@csrf_exempt
def edit_purchase(request, purchase_id):
    purchase = get_object_or_404(Purchase, id_purchase=purchase_id)

    banks = {
        'institution': Bank.objects.all()
    }

    categories = {
    'category': PurchaseCategory.objects.all()
    }

    if request.method == 'POST':
        purchase.product = request.POST.get('product')
        purchase.purchase_category = PurchaseCategory.objects.get(pk=request.POST.get('category_id'))
        purchase.bank =  Bank.objects.get(pk=request.POST.get('bank_id'))
        purchase.payment_type = request.POST.get('payment_type')
        purchase.total_value = request.POST.get('total')
        purchase.purchase_date = request.POST.get('purchase_date')
        purchase.save()
        return redirect('list_purchase')  # Redireciona para a página de listagem de purchaseorias

    return render(request, 'purchase/edit_purchase.html', {"purchase": purchase, "banks" : banks, "categories" : categories})
