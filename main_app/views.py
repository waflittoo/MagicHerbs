from django.shortcuts import render
from .models import Product, Travel
# Create your views here.

def index(request):
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