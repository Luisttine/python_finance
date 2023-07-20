from django.shortcuts import render
from .models import PurchaseCategory

def home(request):
    return render(request, 'home/home.html')

def add_category(request):
    new_category = PurchaseCategory()
    new_category.category_name = request.POST.get('nome')
    new_category.save()
    return render(request, 'category/add_category.html')

def category(request):
    
    category = {
        'category': PurchaseCategory.objects.all()
    }

    return render(request, 'category/list_category.html', category)