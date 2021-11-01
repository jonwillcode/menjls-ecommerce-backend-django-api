from django.contrib import admin
from django.contrib.admin.decorators import register
from django.db.models.aggregates import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode

from .models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['category']
    prepopulated_fields = {
        'slug': ['name']
    }
    list_display = ['name', 'category_name',
                    'price', 'date_added', 'display_to_customer']
    list_editable = ['price']
    list_per_page = 20
    search_fields = ['name']
    list_select_related = ['category']

    def category_name(self, product):
        return product.category.name


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'products_count', 'display_to_customer']
    prepopulated_fields = {
        'slug': ['name']
    }
    search_fields = ['name']

    @admin.display(ordering='products_count')
    def products_count(self, category):
        url = (
            reverse('admin:product_product_changelist')
            + '?'
            + urlencode({
                'category__id': str(category.id)
            })
        )
        return format_html('<a href={}">{}</a>', url, category.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('products')
        )
