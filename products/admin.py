from django.contrib import admin

# Register your models here.
from django.contrib import admin

from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'features','price')


admin.site.register(Product, ProductAdmin)
