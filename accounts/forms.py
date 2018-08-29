from django import forms
from .models import Profile
        
class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['first_name', 'last_name', 'email', 'phone_number', 'country', 'postcode', 'city', 'street_address1', 'street_address2', 'county', 'newsletter_subscription', 'image']

