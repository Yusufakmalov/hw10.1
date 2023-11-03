from django.contrib import admin

# Register your models here.
from shop2.models import ProductModel, FormModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'created_at']
    search_fields = ['title', 'price']
    list_filter = ['created_at']

@admin.register(FormModel)
class FormModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'age', 'comment']
