from django.shortcuts import render, redirect
from .models import Product, Travel
from .forms import ContactForm

from django.core.mail import send_mail
from django.template.loader import render_to_string

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
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print('valid mail')

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            html = render_to_string('./emails/email_template.html', {
                'name': name,
                'email': email,
                'message': message,
            })

            send_mail('Contact Form', 'Contact Form', 'magic.herbs.contacto@gmail.com', ['ivan.prueba.python@gmail.com'], html_message=html)
            return redirect('contact')
    else:
        form = ContactForm()

    param = {
        'form': form,
    }
    return render(request, 'contact.html', param)


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

def payments_page(request, product_type, product_id):

    render_page = 'payment_pages.html'
    if product_type == 'travel':
        render_page = 'payment_travel.html'
        param ={
            'prod_id': product_id,
            'month': range(12),
            'year': range(10),
        }
    elif product_type == 'item':
        render_page = 'payment_item.html'


    return render(request, render_page, param)
