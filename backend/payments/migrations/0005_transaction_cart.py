# Generated by Django 5.1.7 on 2025-04-30 18:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_cart_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions', to='payments.cart'),
        ),
    ]
