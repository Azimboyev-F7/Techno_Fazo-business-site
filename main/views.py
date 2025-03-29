from django.shortcuts import render
from .models import Product, Kop_sotilgan_tovar, Kirishdagi_tovar


# Create your views here.

def index(request):
    products = Product.objects.all()
    kirishdagi = Kirishdagi_tovar.objects.all()
    context = {
        'products': products,
        'kirishdagi': kirishdagi
    }
    return render(request, 'texno_fazo/index.html', context)


def industry(request):
    context = {
        
    }
    return render(request, 'texno_fazo/industries.html', context)

def product_list(request):

    context = {

    }
    return render(request, 'texno_fazo/product_details.html', context)

def shop(request):
    products = Product.objects.all()
    cheap_products = Product.objects.all().order_by('price')
    popular_products = Kop_sotilgan_tovar.objects.all()
    context = {
        'products': products,
        'cheap_products': cheap_products,
        'popular_products': popular_products
    }
    return render(request, 'texno_fazo/shop.html', context)

def about(request):
    context = {

    }
    return render(request, 'texno_fazo/about.html', context)

def blog(request):
    context = {

    }
    return render(request, 'texno_fazo/blog.html', context)

def contact(request):

    context = {

    }
    return render(request, 'texno_fazo/contact.html', context)


