from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm, PaymentForm
from .models import OrderLineItem, Order
from products.models import Product
from cart.utils import get_cart_items_and_total
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required()   
def show_checkout(request):
    payment_form = PaymentForm()
    cart = request.session.get('cart', {})
    context = get_cart_items_and_total(cart)
    context.update({'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE_KEY})
    return render(request, "checkout/checkout.html", context)


@login_required()    
def confirm_checkout(request):
    order_form = OrderForm(request.POST)
    payment_form = PaymentForm(request.POST)
    
    if order_form.is_valid() and payment_form.is_valid():
        order = order_form.save(commit=False)
        
        if request.user.profile:
            order.profile = request.user.profile
        
        order.save()
        
        cart = request.session.get('cart', {})
        
        for order_id, basket in cart.items():
            line_item = OrderLineItem(
                order=order,
                product_id = basket['id'],
                quantity = basket['quantity'], 
                weight = basket['weight'],
                )
            line_item.save()
        
        items_and_total = get_cart_items_and_total(cart)
        total = items_and_total['total']
        stripe_token=payment_form.cleaned_data['stripe_id']

        total_in_cent = int(total*100)
        
        try:
            charge = stripe.Charge.create(
                amount=total_in_cent,
                currency="EUR",
                description="Dummy Transaction",
                card=stripe_token,
            )
        
        except:
            messages.error(request, "Error Charging Credit Card")
            return redirect('show_checkout')      
      
        if charge.paid:
            messages.error(request, "You have successfully paid")
            del request.session['cart']
            return redirect("show_home")
        else:
            return HttpResponse("Charge Not Paid")
    
    else:
        print(order_form.errors)
        cart = request.session.get('cart', {})
        context = get_cart_items_and_total(cart)
        context.update({'form': form})
    
        return render(request, "checkout/checkout.html",  context)