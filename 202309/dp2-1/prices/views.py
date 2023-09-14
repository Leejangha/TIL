from django.shortcuts import render
from .data import product_price

# Create your views here.
def price(request, thing, cnt):
    if thing in product_price:
        price = product_price[thing]*cnt
    else:
        price = False
    
    context = {
        'thing': thing,
        'cnt': cnt,
        'price': price,
    }
    return render(request, 'prices/price.html', context)