from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'created_at')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    list_per_page = 10
    date_hierarchy = 'created_at'
    ordering = ('-id', )
    readonly_fields = ('created_at', 'updated_at', 'slug')
    # prepopulated_fields = {'slug': ('title',)}

admin.site.register(Product, ProductAdmin)
    