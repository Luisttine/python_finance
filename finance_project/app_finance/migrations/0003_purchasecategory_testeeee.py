# Generated by Django 2.2.12 on 2023-07-20 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_finance', '0002_remove_purchasecategory_teste'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasecategory',
            name='testeeee',
            field=models.TextField(default='default', max_length=255),
            preserve_default=False,
        ),
    ]
