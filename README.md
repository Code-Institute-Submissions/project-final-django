# project-final-django
This is an ecommerce website built for a **fictional** cheese company. It is built in the Django framework and uses Stripe as a payment system. The web app allows users to register, add products (cheeses) to their shopping cart, checkout the shopping cart,  and, see their complete order history.  

## Live demo
A live demo of the web app can be viewed clicking this link: https://sdv-the-cheese-factory.herokuapp.com/

## Built with
1. Django
2. Python
3. HTML5
4. CSS3
5. JavaScript
6. SQLite
7. Bootstrap 

## Django components
This web app is built in Django, a Python based framework for building web applications. This section briefly explains how this framework is applied in the project. 

#### Apps
The project contains five django apps. All apps have their own specific function. This section briefly explains what the app does for the user. After this section there will be more explanation on the files inside the apps. 
###### Products
The products app displays all the products in the webshop and allows the user to narrow down their search for a product. Users can also see more details of a specified product and can add products to the cart. 
###### Cart
The cart shows all products that are ready for checkout. It displays them in a table with their respective information on for example queantity and price. Also, a total price is calculated and users can remove items from the cart. 
###### Checkout
The checkout allows users to fill in their shipping and billing information. It also shows a summary of the products they are going to buy. All information, except for the payment details, are prefilled through using the profiles of the users (later more on this). 
###### Accounts
The accounts app allows people to register. Users that are already registered and visit the site are allowed to login. If people forgot their password they can request a new password. A link will be sent to the emailaddress they fill in. Clicking on this link brings them to a page where they can enter a new password and redirects them back to the website. 
The account app also allows users to view their complete order history selected on date starting with the most recent order. 
###### Home
The Home app contains the home page, the about-us page and the contact page. On the contact page people can fill in a form that sents an email to the company containing their comment. The contact page also embeds google maps with the company's address pinned down. 

#### URL's
The url.py files direct the url's to specified views. All Django apps have their own url.py file. The central url.py in the 'webshop' directory imports all the urls from the apps through the include method. Importing all the urls from their respective apps creates order in the project. 

```python
from products import urls as products_urls
```

```python
urlpatterns = [
  path('products/', include(products_urls))
]
```

#### Views
the url.py files usually direct to a certain view in the views.py files. The views are python functions that determine how the website works. Most importantly, a view renders a specific html template. Another important task is making queries to the database. For example, the view that allows users to see their order history makes a query to the database and then returns the right html template with the relevant orders: 

```python
def show_order_history(request):
    orders = Order.objects.all().filter(profile = request.user.profile).order_by('-date')
    return render(request, "accounts/orderhistory.html", {'orders': orders})
```

#### Templates
The templates are the different html pages that are rendered by the views. Every app has its own templates directory with the relevant html pages for that app. 
This project also uses the Django Template Language for preventing unesseccary repetition of elements that must be visible on multiple webpages, most importantly the <head>, navbar and footer. the base.html file in the templates directory on the top level contains this code. It also contains the following Django Template Language: 
  
```python
{% block content %}
{% endblock %}
```
This block allows for code insertions inside. Other html pages can put their code inside the block through extending on it like so: 

```python
{% extends 'base.html' %} {% block content %}
code here
{% endblock %}
```

#### Models
The models.py files are used for creating tables in the relational database. Django creates tables from the classes that are written in models.py. 
In this project there are tables created for a User, a Profile, a Product, an Order, and an OrderLineItem. See for example the code for creating the Order class: 

```python
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
```

One thing must be noted by the above code snippet. Both the Order and the Profile model contain columns that store the same information, for example street_address and phone_number. This is done purposively in order to store the user information as it was at the time of ordering. When there exists only a one to one relationship with the Profile table, then instances of an Order would change when a user changes his or her profile. This could lead to situations that should be avoided. As an example see the way the price is stored in the Order model. Changing the price of cheese would now lead to changes in the price in the order history. In order to fix this bug the price as it was at the time of ordering must be stored. 



## Authors

## Acknowledgements 
