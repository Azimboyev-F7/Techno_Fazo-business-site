# Generated by Django 5.1.7 on 2025-03-28 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_slug_alter_product_image_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kop_sotilgan_tovar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('price', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='product/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
