from django.db import models
from products.models import Product
from accounts.models import Profile
from django.contrib.auth.models import User
from django.utils import timezone

class Order(models.Model):
    profile = models.ForeignKey(Profile, related_name='orders', null=True, blank=False, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=40, blank=False)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=40, blank=False)
    street_address_1 = models.CharField(max_length=40, blank=False)
    street_address_2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField(auto_now_add=True)
    
    @property
    def total(self):
        total = 0 
        items = self.line_items.all()
        for item in items: 
            total += item.total
        return total 
            
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.last_name)
        
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, related_name="line_items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, related_name="orders", on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)
    weight = models.IntegerField(blank=False)

    @property
    def total(self):
        return self.quantity * self.weight * self.product.price 
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)