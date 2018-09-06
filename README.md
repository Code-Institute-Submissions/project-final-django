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
path('products/', include(products_urls))
```
