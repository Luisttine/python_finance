from django.db import models

class PurchaseCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.TextField(max_length=255)
    testeeee = models.TextField(max_length=255)

