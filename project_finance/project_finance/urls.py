"""
URL configuration for finance_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from polls import views

urlpatterns = [
    path('', views.home, name='home'),

    # Category Paths
    path('add_category', views.add_category, name='add_category'),
    path('category', views.category, name='category'),
    path('list_categ', views.list_categ, name='list_categ'),

    # Bank Paths
    path('add_bank', views.add_bank, name='add_bank'),
    path('bank', views.bank, name='bank'),
    path('list_bank', views.list_bank, name='list_bank'),

    # Purchase Paths
    path('add_purchase', views.add_purchase, name='add_purchase'),
    path('purchase', views.purchase, name='purchase'),
    path('list_purchase', views.list_purchase, name='list_purchase'),
]
