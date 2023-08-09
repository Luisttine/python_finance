from django.urls import path
from polls import views

urlpatterns = [
    path('', views.home, name='home'),

    # Category Paths
    path('add_category', views.add_category, name='add_category'),
    path('category', views.category, name='category'),
    path('list_categ', views.list_categ, name='list_categ'),
    path('delete_categ/<int:category_id>', views.delete_categ, name='delete_categ'),

    # Bank Paths
    path('add_bank', views.add_bank, name='add_bank'),
    path('bank', views.bank, name='bank'),
    path('list_bank', views.list_bank, name='list_bank'),
    path('delete_bank/<int:bank_id>', views.delete_bank, name='delete_bank'),

    # Purchase Paths
    path('add_purchase', views.add_purchase, name='add_purchase'),
    path('purchase', views.purchase, name='purchase'),
    path('list_purchase', views.list_purchase, name='list_purchase'),
    path('delete_purchase/<int:purchase_id>', views.delete_purchase, name='delete_purchase'),

]
