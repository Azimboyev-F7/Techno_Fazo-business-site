from django.urls import path

from .views import index, industry

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('industry/', industry, name='industry'),
]
