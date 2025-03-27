from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    list_per_page = 10
    readonly_fields = ('created_at', 'updated_at', 'slug')

admin.site.register(Product, ProductAdmin)
    