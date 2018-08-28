from django.shortcuts import render, redirect, get_object_or_404
from .utils import get_cart_items_and_total

# Create your views here.
def show_cart(request):
    cart = request.session.get('cart', {})
    context = get_cart_items_and_total(cart)
    
    return render(request, "cart/cart.html", context)
    
def add_to_cart(request):
    product_id = request.POST['id']
    quantity = int(request.POST['quantity'])
    weight = int(request.POST['weight'])

    key = "{0}-{1}".format(product_id, weight)

    cart = request.session.get('cart', {})

    item = cart.get(key, {'id': product_id, 'quantity': 0, 'weight': weight})    
    item['quantity'] = item['quantity'] + quantity
    
    cart[key] = item
    
    request.session['cart'] = cart
    print(cart)
    
    return redirect('products_list')
    
def remove_item(request):
    id = request.POST['id']
    
    cart = request.session.get('cart', {})
    del cart[id]
    request.session['cart'] = cart

    return redirect('show_cart')