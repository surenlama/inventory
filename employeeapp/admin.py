from django.contrib import admin
from employeeapp.models import Category,Store,Product,Order
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Store)
admin.site.register(Order)