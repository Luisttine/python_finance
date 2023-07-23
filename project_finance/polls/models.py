from django.db import models

class PurchaseCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.TextField(max_length=255)

    def __str__(self):
        return self.category_name    

class MonthlyExpanse(models.Model):
    id = models.AutoField(primary_key=True)
    institution_id = models.ForeignKey(
        "PurchaseCategory",
        on_delete=models.CASCADE,
    )
    purchase_category = models.ForeignKey(
        "PurchaseCategory",
        on_delete=models.CASCADE,
    )
    payment_type = models.TextField(max_length=12)
    total_value = models.FloatField()
    purchase_date = models.DateField

    def __str__(self):
        return self.payment_type   