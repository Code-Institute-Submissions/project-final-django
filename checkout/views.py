from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm, PaymentForm
from .models import OrderLineItem
from products.models import Product
from cart.utils import get_cart_items_and_total
from django.conf import settings
from django.contrib import messages
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def show_checkout(request):
    order_form = OrderForm()
    payment_form = PaymentForm()
    cart = request.session.get('cart', {})
    context = get_cart_items_and_total(cart)
    context.update({'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE_KEY})
    return render(request, "checkout/checkout.html", context)