from django.contrib import admin

from store.models import Product, Collection

# Register your models here.
admin.site.register(Collection)
admin.site.register(Product)
