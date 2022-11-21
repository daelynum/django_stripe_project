from django.contrib import admin

from shop.models import Item


class AdminItem(admin.ModelAdmin):
    list_display = ('item_id', 'name', 'description', 'price')
    search_fields = ['name', 'description']


admin.site.register(Item, AdminItem)
