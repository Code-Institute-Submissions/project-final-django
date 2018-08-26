from django.urls import path
from .views import show_cart, add_to_cart, remove_item

urlpatterns = [
    path('', show_cart, name='show_cart'),   
    path('add/', add_to_cart, name='add_to_cart'),
    path('remove/', remove_item, name="remove_item"),
]