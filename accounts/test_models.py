from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

class TestProfileModel(TestCase):
    
    def test_newsletter_subscription_defaults_to_False(self):
        user_profile = User(username="stein", password="asdlfj")
        user_profile.save()
        item = Profile(user=user_profile, first_name="test", last_name="test", email="test@example.com", phone_number="0324", country="nl", postcode="342", city="test", street_address1="test", street_address2="test")
        item.save()
        self.assertEqual(item.first_name, "test")
        self.assertFalse(item.newsletter_subscription)
        