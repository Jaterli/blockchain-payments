# Generated by Django 5.1.7 on 2025-03-19 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
