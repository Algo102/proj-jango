# Generated by Django 5.0.6 on 2024-06-24 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw_app4', '0002_product_order_orderitem_order_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
