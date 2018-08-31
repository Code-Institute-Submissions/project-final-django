from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.template.loader import get_template
from django.contrib import messages, auth


# Create your views here.
def show_home(request):
    return render(request, "home/home.html")
    
def show_contact(request):
    return render(request, "home/contact.html")
    
def submit_contact_form(request):
    
    
        contact_name = request.POST.get('contact_name', '')
        contact_email = request.POST.get('contact_email', '')
        form_content = request.POST.get('content', '')
        template=get_template('home/contact_template.txt')
        context = {
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_content': form_content,
        }
        content = template.render(context)
            
        subject = 'Thanks for getting in touch!'
        message = 'We will get back to you asap'
        from_email = settings.EMAIL_HOST_USER
        to_email = [contact_email]
        send_mail(subject,message,from_email,to_email,fail_silently=False)
        email = EmailMessage(
            "New contact form message",
            content,
            "Your website" +'',
            ['steindevos@gmail.com'],
            headers = {'Reply-To': contact_email }
        )
        email.send()
        messages.success(request, 'Thank you. We have received your message and will get back to you as soon as possible.')
        
        return redirect('show_contact')
        
def show_about_us(request): 
    return render(request, "home/about-us.html")