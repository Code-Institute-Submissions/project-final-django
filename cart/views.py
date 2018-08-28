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
    print('---------------------------------------------------')
    print(weight)

    cart = request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + quantity
    
    request.session['cart'] = cart
    print(cart)
    
    return redirect('products_list')
    
def remove_item(request):
    id = request.POST['id']
    
    cart = request.session.get('cart', {})
    del cart[id]
    request.session['cart'] = cart

    return redirect('show_cart')