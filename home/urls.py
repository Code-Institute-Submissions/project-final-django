from django.urls import path
from .views import show_home, show_contact


urlpatterns = [
    path('', show_home, name="show_home"), 
    path('contact/', show_contact, name="show_contact"),
]