from django.contrib import admin

from .models import *


# class SupplierAdmin(admin.ModelAdmin):
#     list_display = ['user', 'name', 'address', 'created_date']


# class BuyerAdmin(admin.ModelAdmin):
#     list_display = ['user', 'name', 'address', 'created_date']


# admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Delivery)
admin.site.register(Restaurant)
admin.site.register(Food)
