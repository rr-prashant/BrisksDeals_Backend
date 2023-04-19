# Generated by Django 4.1.6 on 2023-03-19 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brisk_app1', '0003_cart_vendor_phone_deals_business_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='couponactive',
            name='deal_applicable_day',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='couponactive',
            name='deal_applicable_time',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='couponactive',
            name='deal_expiry_date',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='couponactive',
            name='deal_title',
            field=models.CharField(blank=True, max_length=70),
        ),
    ]