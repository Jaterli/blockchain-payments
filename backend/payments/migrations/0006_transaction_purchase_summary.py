# Generated by Django 5.1.7 on 2025-05-04 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_transaction_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='purchase_summary',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
