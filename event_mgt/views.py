from django.shortcuts import render, redirect
from .forms import BookingForm
# Create your views here.
from django.http import HttpResponse
from.models import Event, Contact




def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def events(request):
    dict_eve={
        'eve':Event.objects.all()
    }
    return render(request,"events.html",dict_eve)

def booking(request):

    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')



    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,"booking.html", dict_form)

def contact(request):
    if request.method == 'POST':
        contact = Contact()  # Instantiate a Contact object
        name = request.POST.get('name')  # Use parentheses () instead of square brackets []
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        return HttpResponse('<h1>Thank You For Contacting Us</h1>')  # Provide a response after saving the contact
    
    return render(request, "contact.html")