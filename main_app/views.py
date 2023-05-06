from django.shortcuts import render
from .models import Product, Travel
# Create your views here.

def index(request):
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip:
        ip = user_ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
        print(f"Direccion ip: {ip}")
    return render(request, 'index.html')


def products(request):
    product_list = Product.objects.all() 
    param = {
        'product_list': product_list,
    }
    return render(request, 'products.html', param)


def travel(request):
    travel_list = Travel.objects.all()
    param = {
        'travel_list': travel_list,
    }
    return render(request, 'travel.html', param)


def legal(request):
    return render(request, 'legal.html')


def contact(request):
    return render(request, 'contact.html')


def product_page(request, product_id):
    product = Product.objects.get(id=product_id)
    param = {
        'product': product,
        'range': range(product.available)
    }

    return render(request, 'product_page.html', param)

def travel_page(request, travel_id):
    travel_i = Travel.objects.get(id=travel_id)
    param = {
        'travel': travel_i,
    }

    return render(request, 'travel_page.html', param)
