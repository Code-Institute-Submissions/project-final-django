from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.
def products_list(request):
    
    if 'category' in request.GET:
        products = Product.objects.filter(category=request.GET['category'])
    else:
        products = Product.objects.all()
        
    return render(request, "products/show_products.html", {'products': products})
    
def product_details(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "products/show_details.html", {'product': product})