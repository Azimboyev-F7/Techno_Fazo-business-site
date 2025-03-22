from django.urls import path

from .views import index, industry, product_list, shop

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('industry/', industry, name='industry'),
    path('product_list/', product_list, name='product_list'),
    path('shop/', shop, name='shop'),
]

