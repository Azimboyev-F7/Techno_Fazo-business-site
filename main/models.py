from django.db import models
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    price = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


    def save(self, insert=False, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.slug is None:
            self.slug = slugify(self.title)
            
        return super().save(force_insert=False, force_update=False, using=None, update_fields=None)
