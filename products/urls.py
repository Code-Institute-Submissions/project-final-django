from django.urls import path
from .views import products_list, product_details

urlpatterns = [
    path('', products_list, name="products_list"), 
    path('<int:id>', product_details, name="product_details"),
]