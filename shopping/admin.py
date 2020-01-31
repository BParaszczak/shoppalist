from django.contrib import admin

from .models import Product, Category, Entry

class ProductAdmin(admin.ModelAdmin):
    product_list = ['name', 'amount', 'unit', 'comment', 'need_date']
    list_filter = ['name', 'need_date']
    date_hierarchy = 'need_date'
    search_fields = ['name']
    ordering = ['name', 'amount', 'unit', 'need_date']
    list_select_related = True

class CategoryAdmin(admin.ModelAdmin):
    category_list = ['name']
    list_filter = ['name']
    search_fields = ['name']
    ordering = ['name']
    list_select_related = True

class EntryAdmin(admin.ModelAdmin):
    entry_date = ['add_date']
    list_filter = ['add_date']
    date_hierarchy = 'add_date'
    ordering = ['add_date']
    list_select_related = True

class EntryInline(admin.TabularInline):
    model = Entry
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = (EntryInline,)

class CategoryAdmin(admin.ModelAdmin):
    inlines = (EntryInline,)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)