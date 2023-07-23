from django.shortcuts import render
from .models import PurchaseCategory
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'home/home.html')

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