from django.db import models

class PurchaseCategory(models.Model):
    id_purchase_category = models.AutoField(primary_key=True)
    category_name = models.TextField(max_length=255)

    def __str__(self):
        return self.category_name
    
class Bank(models.Model):
    id_bank = models.AutoField(primary_key=True)
    institution = models.TextField(max_length=255)
#    debt_value = models.FloatField()
#    credit_value = models.FloatField()

    def __str__(self):
        return self.institution

class Purchase(models.Model):
    id_purchase = models.AutoField(primary_key=True)
    product = models.TextField(max_length=255)
    purchase_category = models.ForeignKey(
        PurchaseCategory,
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