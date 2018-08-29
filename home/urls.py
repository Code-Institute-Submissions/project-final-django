from django.urls import path
from .views import show_home, show_contact, submit_contact_form, show_about_us


urlpatterns = [
    path('', show_home, name="show_home"), 
    path('contact/', show_contact, name="show_contact"),
    path('send/', submit_contact_form, name="submit_contact_form"), 
    path('about-us/', show_about_us, name="show_about_us")
]