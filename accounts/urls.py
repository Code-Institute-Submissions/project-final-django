from django.urls import path, reverse_lazy
from .views import register
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.conf.urls import url

urlpatterns = [
    path('register/', register, name="register"),    
    
    path('login/', login, {'template_name': 'accounts/login.html'}, name='login'),
    path('logout/', logout, name='logout'),
]