from django.db import models

class PurchaseCategory(models.Model):
    id_purchase_category = models.AutoField(primary_key=True)
    category_name = models.TextField(max_length=255)

    def __str__(self):
        return self.category_name
    
class Bank(models.Model):
    id_bank = models.AutoField(primary_key=True)
    institution = models.TextField(max_length=255)
    debt_total_value = models.FloatField()
    credit_total_value = models.FloatField()

    def __str__(self):
        return self.institution
    
class Profile(models.Model):
    id_profile = models.AutoField(primary_key=True)
    profile_name = models.TextField(max_length=255, default='Luis')

    def __str__(self):
        return self.profile_name

class Purchase(models.Model):
    id_purchase = models.AutoField(primary_key=True)
    product = models.TextField(max_length=255)
    purchase_category = models.ForeignKey(
        PurchaseCategory,
        on_delete=models.CASCADE,
    )
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    bank = models.ForeignKey(
        Bank,
        on_delete=models.CASCADE,
    )
    payment_type = models.TextField(max_length=12)
    total_value = models.FloatField()
    purchase_date = models.DateField()

    def __str__(self):
        return self.payment_type