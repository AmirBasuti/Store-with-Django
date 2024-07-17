from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from store.models import Product, Collection, Customer, Order, OrderItem


class inventoryfilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low'),
            ('>=10', 'OK'),
        ]

    def queryset(self, request, queryset):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)
        if self.value() == '>=10':
            return queryset.filter(inventory__gte=10)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title'],
    }
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_filter = ['last_update', 'collection', inventoryfilter]
    search_fields = ['title', 'description']
    autocomplete_fields = ['collection']
    list_select_related = ['collection']
    list_editable = ['unit_price']
    actions = ['clear_inventory']
    date_hierarchy = 'last_update'
    list_per_page = 10

    @admin.action(description='Clear inventory')
    def clear_inventory(self, request, queryset):
        count = queryset.update(inventory=0)
        self.message_user(request, f'{count} products were successfully updated', )

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
    ordering = ['first_name', 'last_name']
    list_editable = ['membership']
    list_filter = ['membership']
    list_per_page = 10

    def orders(self, customer):
        urls = (reverse('admin:store_order_changelist') +
                "?" +
                urlencode({'customer__id': str(customer.id)}))
        return format_html('<a href= "{}">{}</a>', urls, customer.order_set.count())


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_count']
    search_fields = ['title']
    ordering = ['title']
    list_per_page = 10

    @admin.display(ordering='beshmor')
    def product_count(self, collection):
        urls = (reverse('admin:store_product_changelist') +
                "?" +
                urlencode({'collection__id': str(collection.id)}))

        return format_html('<a href= "{}">{}</a>', urls, collection.beshmor)
        # return collection.beshmor

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(beshmor=Count('product'))


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    autocomplete_fields = ['product']
    max_num = 10
    min_num = 1
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ['customer__first_name', 'customer__last_name']
    list_display = ['id', 'placed_at', 'customer']
    list_select_related = ['customer']
    autocomplete_fields = ['customer']
    ordering = ['customer']
    inlines = [OrderItemInline]
    list_per_page = 10
    # ordering = ['placed_at']
    # @admin.display(ordering='placed_at')
    # def customer_name(self, order):
    #     return f'{order.customer.first_name} {order.customer.last_name}'
