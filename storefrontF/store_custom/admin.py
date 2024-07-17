from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from store.admin import ProductAdmin
from store.models import Product
from tags.models import TaggedItem


# Register your models here.
class Tagediteminline(GenericTabularInline):
    model = TaggedItem
    autocomplete_fields = ['tag']
    extra = 0


class CustomeProductAdmin(ProductAdmin):
    inlines = [Tagediteminline]


admin.site.unregister(Product)
admin.site.register(Product, CustomeProductAdmin)
