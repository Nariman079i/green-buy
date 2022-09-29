from django.shortcuts import render
from .models import *
# Create your views here.
def index(requests):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return  render(requests, 'main/index.html', context=context)