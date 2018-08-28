from django.shortcuts import get_object_or_404
from products.models import Product

def get_cart_items_and_total(cart):
    total = 0
    cart_items = []
    for item in cart.values():
      
        product_id = item['id']
        quantity = item['quantity']
        weight = item['weight']
        
        product = get_object_or_404(Product, pk=product_id)
        
        item_total = quantity * weight * product.price
        total += item_total
        cart_items.append({'product':product, 'quantity': quantity, 'weight': weight, 'total': item_total})
        
    return {'cart_items': cart_items, 'total': total}