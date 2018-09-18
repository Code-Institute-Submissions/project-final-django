# project-final-django
This is an ecommerce website built for a **fictional** cheese company. It is built in the Django framework and uses Stripe as a payment system. The web app allows users to register, add products to their shopping cart and checkout the shopping cart.

An import feature of this web application is that customers of the company can - if they are logged in - view their complete order history. This is helpful, because most of the customers are middleman who buy frequently from the company.  

#### Live demo
A live demo of the web app can be viewed clicking this link: https://sdv-the-cheese-factory.herokuapp.com/

## Built with
1. Django
2. Python
3. HTML5
4. CSS3
5. JavaScript
6. JQuery
7. SQLite
8. Bootstrap 
9. Stripe (payment API)
10. SendGrid (email API)

## Features
* Products list - allows users to get an overview of the cheese that is sold by De Producent. They can also make selections. 
* Shopping cart - allows users to get an overview of the cheese they are going to buy. They also have the option to delete some. 
* Checkout - overview of the order and the shipping/payment details. 
* Contact form - allows users to send an email to the company. 
* Profile page- allows users to view their complete order history and change their profile details. 

###### Features left to implement: 
* Blog where farmers will share their experiences (for this reason people are asked to upload a profile image when they register) 

## UX 
This web application is built for De Producent, a cooporation of cheese farmers out of the Netherlands that operates as a wholesale. Most of their customers are middleman. 

The aim for this website was to allow for a quick order/checkout process. Most of the visitors of the website will be market vendors; frequent buyers that are familiar with the products of De Producent. Therefore, the shopping carts have an 'add to cart' so customers do not have to go to the 'more detail' page to order. Furthermore, when the customer wants to checkout the shopping cart, most of the form fields are prefilled. This will also contribute to a fast buying process. 

Again, the assumption is that most of the customers will be frequent buyers. Therefore customers can also see their complete order history on their profile page. They will see how much they have spent, but also what cheese they have bought. 

## Getting Started
This project can be cloned and modified for your own purposes. The following instructions will help you in setting up the project on your own system. 

#### Prerequisites
Make sure you have python installed on your machine. Not sure if you have python installed? Type ```python --version``` in your terminal. 

#### Installing
This is an installation guide for Mac/Linux systems. Windows commands might be slightly different. 
1. Clone the project to your local machine ```git clone git@github.com:steindevos/project-final-django.git```
2. Create and activate a virtual environment. create: ```$ python3 -m venv ~/virtualenvs/<name_of_environment>``` and activate: ```$ source ~/virtualenvs/<name_of_environment>/bin/activate```. 
3. This project uses third party libraries. Install all through pip installing the requirements.txt file. ```pip3 install -r requirements.txt```. 
4. Set up your environment variables in an env.sh file at the top level of the project. Make sure to include this file to the .gitignore file. 
```python
export SECRET_KEY=''
export DEBUG='True'

export STRIPE_PUBLISHABLE_KEY=''
export STRIPE_SECRET_KEY=''

export EMAIL_HOST_USER='your@gmail.com'    
export EMAIL_HOST_PASSWORD='yourPassword'
```
* Create your own [secret_key]. 
* Set up a Stripe account [here] in order to create your own Stripe keys.
* Django comes with the SQLite database. When you run your project for the first time you first have to create the database tables with the following command ```python3 managage.py migrate```. 
* In order to run the project in your browser type ```python3 manage.py run``` in the terminal. In your browser visit ```127.0.0.1:8000``` and there you should see the web application.
* In order to populate the database, first create a superuser ```python3 managage.py createsuperuser```. Now you can login in the admin panel ```127.0.0.1:8000/admin```. In the admin panel you can create your own products and manage the accounts, orders and profiles.

[secret_key]: https://www.miniwebtool.com/django-secret-key-generator/
[here]: https://stripe.com/gb

#### Running tests
Important parts of the web application are tested through automated unit tests. The tests are created with TestCase, which is part of the Django framework. 
The tests can be found inside the test_.py files inside the app directories. In order to run the tests type ```python3 manage.py test``` in the command line.

It is also important to perform some functional tests. Try to create a new user and add some products to your cart. Test the checkout by filling in the following dummy credit card details 
```Card card number: 4242424242424242```
```Security code: 100```


#### Deployment
This web app is deployed on [Heroku] and uses its Postgres database. The media files are stored in an Amazon s3 bucket. 

[Heroku]: https://www.heroku.com/

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
This web app is created by Stein de Vos. 

## Acknowledgements
For the styling the bootswatch [Litera theme] is used.

Much of the content comes from the [actual] website of the Producent. 

[actual]: http://deproducent2017.nl/ 

[Litera theme]: https://bootswatch.com/litera/

Also, this web app could have never been build without the guidance of the teachers of the Code Institute. In particular Matt, Brian, Richard and Katie. Thanks for your teachings! 
