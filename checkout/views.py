from django.shortcuts import render

# Create your views here.
def show_checkout(request):
    return render(request, "checkout/checkout.html")