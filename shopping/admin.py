from django.contrib import admin

from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    product_list = ['name', 'amount', 'unit', 'comment', 'need_date']
    list_filter = ['name', 'need_date']
    