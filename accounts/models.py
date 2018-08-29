from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    phone_number = models.IntegerField()
    country = models.CharField(max_length=20)
    postcode = models.CharField(max_length=15)
    city = models.CharField(max_length=20)
    street_address1 = models.CharField(max_length=40)
    street_address2 = models.CharField(max_length=40)
    county = models.CharField(max_length=20)
    newsletter_subscription = models.BooleanField(default=False)
    image = models.ImageField(upload_to="avatars", default="avatars/anonymous.png")
    
    def __str__(self):
        return self.user.username + ' Profile'