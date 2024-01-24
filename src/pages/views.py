from django.db.models import Q
from django.shortcuts import render

from product.models import Category, Product


def home(request):
    products = Product.objects.all()[0:8]
    context = {
        'products': products
    }
    return render(request, 'index.html', context)


def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    active_category = request.GET.get('category', '')
    if active_category:
        products = products.filter(category__slug=active_category)
    query = request.GET.get('query', '')
    if query:
        products = products.filter(name__icontains=query)
    context = {

        'categories': categories,
        'products': products,
        'active_category': active_category
    }
    return render(request, 'shop.html', context)


def faq_view(request):
    return render(request, "faq.html")
