from django.urls import path
from polls import views

urlpatterns = [
    path('', views.home, name='home'),

    # Category Paths
    path('add_category', views.add_category, name='add_category'),
    path('category', views.category, name='category'),
    path('list_categ', views.list_categ, name='list_categ'),
    path('delete_categ/<int:category_id>', views.delete_categ, name='delete_categ'),
    path('edit_categ/<int:category_id>', views.edit_categ, name='edit_categ'),

    # Bank Paths
    path('add_bank', views.add_bank, name='add_bank'),
    path('bank', views.bank, name='bank'),
    path('list_bank', views.list_bank, name='list_bank'),
    path('delete_bank/<int:bank_id>', views.delete_bank, name='delete_bank'),
    path('edit_bank/<int:bank_id>', views.edit_bank, name='edit_bank'),

    # Purchase Paths
    path('add_purchase', views.add_purchase, name='add_purchase'),
    path('purchase', views.purchase, name='purchase'),
    path('list_purchase', views.list_purchase, name='list_purchase'),
    path('delete_purchase/<int:purchase_id>', views.delete_purchase, name='delete_purchase'),
    path('edit_purchase/<int:purchase_id>', views.edit_purchase, name='edit_purchase'),

    path('add_profile', views.add_profile, name='add_profile'),
    path('profile', views.profile, name='profile'),
    path('list_profile', views.list_profile, name='list_profile'),
    path('delete_profile/<int:profile_id>', views.delete_profile, name='delete_profile'),
    path('edit_profile/<int:profile_id>', views.edit_profile, name='edit_profile'),

]
