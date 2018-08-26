from django.shortcuts import redirect
from django.contrib import messages
import stripe

def charge_creditcard(total_in_cent, stripe_token):
    try:
        charge = stripe.Charge.create(
            amount=total_in_cent,
            currency="EUR",
            description="Dummy Transaction",
            card=stripe_token,
        )
        
    except:
        messages.error(request, "Error Charging Credit Card")
        return redirect('home')
        
    return charge 
        