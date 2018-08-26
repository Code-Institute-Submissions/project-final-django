from django.urls import path
from .views import show_home


urlpatterns = [
    path('', show_home, name="show_home"),    
]