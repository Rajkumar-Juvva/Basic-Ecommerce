# Generated by Django 4.2 on 2023-04-20 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0007_remove_cart_user_cart_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'My Model', 'verbose_name_plural': 'Products to select'},
        ),
    ]
