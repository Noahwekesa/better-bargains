from django.shortcuts import render


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return render(request, 'cart/partials/menu_cart.html')
