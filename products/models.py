from django.db import models

# Create your models here.

CATEGORY = [
    ['Farmhouse cheese', 'farmhouse'], 
    ['Herb cheese', 'herbs'],
    ['Our brand', 'our brand'],
    ['Specialties', 'specialties']] 

MILK_TYPE = [
    ['Cow', 'cow'], 
    ['Goat', 'goat'],
    ['Sheep', 'sheep']] 

MILK_SANITATION = [
    ['Raw milk', 'none'], 
    ['Thermized', 'thermized'],
    ['Pasteurized', 'pasteurized']]
    
FAT_CONTENT = [
    ['30+', '30+'], 
    ['48+', '48+'],
    ['50+', '50+']]

RIPENING = [
    ['4-8 weeks', '4-8 weeks'], 
    ['8-12 weeks', '8-12 weeks'],
    ['2-3 months', '2-3 months'],
    ['4-7 months', '4-7 months'], 
    ['7-10 months', '7-10 months'],
    ['10-12 months', '10-12 months'],
    ['14+ months', '14+ months'], 
    ['2-12 months', '2-12 months'],
    ['2-14+ months', '2-14+ months']]

class Weight(models.Model):
    kg = models.IntegerField(blank=False, null=False)
    
    def __str__(self):
        return "{0} kg".format(self.kg)    
    

class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    category = models.CharField(max_length=16, choices=CATEGORY, default='Farmhouse cheese', blank=False, null=False)
    description = models.TextField(max_length=400, default="Enter description")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='product_images', default='generic_product.png')
    milk_type = models.CharField(max_length=12, choices=MILK_TYPE, default="Cow", blank=False, null=False)
    milk_sanitation = models.CharField(max_length=12, choices=MILK_SANITATION, default="Raw milk", blank=False, null=False)
    fat_content = models.CharField(max_length=4, choices=FAT_CONTENT, default="48+", blank=False, null=False)
    ripening = models.CharField(max_length=16, choices=RIPENING, default="2-14+ months", blank=False, null=False)
    available_weights = models.ManyToManyField(Weight)

    def __str__(self):
        return self.name    

