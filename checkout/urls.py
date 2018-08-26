from django.urls import path
from .views import show_checkout, confirm_checkout


urlpatterns = [
    path('', show_checkout, name="show_checkout"), 
    path('confirm/', confirm_checkout, name="confirm_checkout"),
]