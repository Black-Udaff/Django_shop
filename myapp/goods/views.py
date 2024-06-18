from django.shortcuts import render
from .goods_list import goods
# Create your views here.


def catalog(request):
    context = {
        'title': 'Home - Каталог',
        'goods': goods,


    }
    return render(request, 'goods/catalog.html', context)


def product(request):
    return render(request, 'goods/product.html')
