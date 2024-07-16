from django.contrib import admin

from store.models import Product, Collection, Customer, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    search_fields = ['title', 'description']
    list_filter = ['last_update', 'collection']
    date_hierarchy = 'last_update'
    # ordering = ['inventory']
    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'


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

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']
    list_select_related = ['customer']
    list_per_page = 10
    search_fields = ['customer__first_name', 'customer__last_name']
    # ordering = ['placed_at']
    ordering = ['customer']
    # @admin.display(ordering='placed_at')
    # def customer_name(self, order):
    #     return f'{order.customer.first_name} {order.customer.last_name}'
