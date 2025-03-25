from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
