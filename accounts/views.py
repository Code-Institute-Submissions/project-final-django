from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileRegistrationForm
from .models import Profile
from checkout.models import Order

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        profile_form = ProfileRegistrationForm(request.POST, request.FILES)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('show_home')
    
    else:
        form = UserCreationForm()
        profile_form = ProfileRegistrationForm()
    return render(request, "accounts/register.html", {'form': form, 'profile_form': profile_form})


@login_required() 
def show_profile(request):
    profile = get_object_or_404(Profile, pk=request.user.profile.id)
    
    if request.method == "POST":
        form = ProfileRegistrationForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            post = form.save()
            return redirect("show_profile") 
        else:
            return render(request, "accounts/profile.html", {"form": form})
    
    else: 
        profile_form = ProfileRegistrationForm(instance=profile)
        return render(request, "accounts/profile.html", {'profile_form': profile_form})

def show_order_history(request):
    orders = Order.objects.all().filter(profile = request.user.profile)
    return render(request, "accounts/orderhistory.html", {'orders': orders})

    