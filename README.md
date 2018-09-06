# project-final-django
This is an ecommerce website built for a **fictional** cheese company. It is built in the Django framework and uses Stripe as a payment system. The web app allows users to register, add products (cheeses) to their shopping cart, checkout the shopping cart,  and, see their complete order history.  

## Live demo
A live demo of the web app can be viewed clicking [this] link (sdv-the-cheese-factory.herokuapp.com). 

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
