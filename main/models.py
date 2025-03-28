from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save

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
    
class Kop_sotilgan_tovar(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    price = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    # def save(self, insert=False, force_insert=False, force_update=False, using=None, update_fields=None):
    #     if self.slug is None:
    #         self.slug = slugify(self.title)
            
    #     return super().save(force_insert=False, force_update=False, using=None, update_fields=None)
    

def product_pre_save(sender, instance,  *args, **kwargs):
    instance.slug = slugify(instance.title)
    if Product.objects.filter(slug=instance.slug).exclude(id=instance.id).exists():
        import uuid
        instance.slug += f"-{str(uuid.uuid4()).split('-')[0]}"
    

pre_save.connect(product_pre_save, sender=Product)
