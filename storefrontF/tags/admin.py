from django.contrib import admin

from tags.models import Tag


# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['lable']
    search_fields = ['lable']
    ordering = ['lable']
    list_per_page = 10
    list_filter = ['lable']
