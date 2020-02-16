from django.contrib import admin

from .models import Product, Category, Entry

class EntryInline(admin.TabularInline):
    model = Entry
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount', 'unit', 'comment']
    list_filter = ['name']
    search_fields = ['name']
    ordering = ['name', 'amount', 'unit']
    list_select_related = True
    inlines = (EntryInline,)

class CategoryAdmin(admin.ModelAdmin):
    category_list = ['name']
    list_filter = ['name']
    search_fields = ['name']
    ordering = ['name']
    list_select_related = True
    inlines = (EntryInline,)

class EntryAdmin(admin.ModelAdmin):
    entry_date = ['add_date']
    list_filter = ['add_date']
    date_hierarchy = 'add_date'
    ordering = ['add_date']
    list_select_related = True

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)