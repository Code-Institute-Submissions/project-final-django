from django.shortcuts import render

# Create your views here.
def show_home(request):
    return render(request, "home/home.html")
    
def show_contact(request):
    return render(request, "home/contact.html")