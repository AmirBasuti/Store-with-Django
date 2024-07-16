from django.contrib import admin

from store.models import Product, Collection, Customer


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'unit_price']
    list_editable = ['unit_price']
    list_per_page = 10
    search_fields = ['title', 'description']
    list_filter = ['last_update', 'collection']
    date_hierarchy = 'last_update'


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10
    search_fields = ['first_name', 'last_name']
    list_filter = ['membership']
    ordering = ['first_name', 'last_name']
# Register your models here.

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured_product']
    list_editable = ['featured_product']
    list_per_page = 10
    search_fields = ['title']
    ordering = ['title']
# admin.site.register(Collection)
# /admin.site.register(Product)
