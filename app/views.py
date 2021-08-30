"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.core.mail import send_mail

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    #assert isinstance(request, HttpRequest)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        company = request.POST.get('company')
        phonenumber = request.POST.get('phonenumber')
        message = request.POST.get('message')
        subject = name+(" From ")+company+(" is Interested In ROPRA product/service")

        data = {
            'name': name,
            'email': email,
            'company': company,
            'phonenumber': phonenumber,
            'message': message,
            'subject': subject,
        }

        message = '''
        From: {} 

        Email: {}

        Company: {}

        Phone Number: {}

        {}
        '''.format(data['name'], data['email'], data['company'], data['phonenumber'], data['message'])
        send_mail(data['subject'], message, '', ['magarciar931@gmail.com'])

    return render(
        request,
        'app/contact.html',
        {
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'year':datetime.now().year,
        }
    )

def services(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/services.html',
        {
            'year':datetime.now().year,
        }
    )

def blog(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        {
            #'title':'Blog',
            #'message':'Technology is Changing Businesses For The Better',
            'year':datetime.now().year,
        }
    )

def whatisauto(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Blog/whatisauto.html',
        {
            'year':datetime.now().year,
        }
    )