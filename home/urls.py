from django.urls import path
from .views import show_home, show_contact, submit_contact_form


urlpatterns = [
    path('', show_home, name="show_home"), 
    path('contact/', show_contact, name="show_contact"),
    path('send/', submit_contact_form, name="submit_contact_form"), 
]