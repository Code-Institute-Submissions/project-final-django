from django.test import TestCase
from .forms import ProfileRegistrationForm


class TestContactForm(TestCase):
    def test_form_is_valid(self):  
        form = ProfileRegistrationForm({
            "first_name": 'Stein',
            "last_name": "de Vos",
            "email": 'steindevos@example.com',
            "phone_number": '06123456789',
            "country": "Netherlands",
            "postcode": "2332ER",
            "city": "Leiden",
            "street_address1": "Lopikerweg 100",
            "street_address2": "Lopik",
            "county": "Zuid Holland", 
            "newsletter_subscription": True, 
        })
        self.assertTrue(form.is_valid())
        
    def test_email_needs_atsymbol(self):
        form = ProfileRegistrationForm({
            "first_name": 'Stein',
            "last_name": "de Vos",
            "email": 'steindevosexample.com',
            "phone_number": '06123456789',
            "country": "Netherlands",
            "postcode": "2332ER",
            "city": "Leiden",
            "street_address1": "Lopikerweg 100",
            "street_address2": "Lopik",
            "county": "Zuid Holland", 
            "newsletter_subscription": True, 
        })
        self.assertFalse(form.is_valid())
            
        
        
    
    