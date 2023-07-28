from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Eventcreation, Rsvp
from templates import *

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


def HomePage(request):
    if request.method == 'POST':
        # Create Event
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        time = request.POST.get('time')
        location = request.POST.get('location')
        organizer = request.POST.get('organizer')
        event = Eventcreation.objects.create(
            title=title,
            description=description,
            date=date,
            time=time,
            location=location,
            organizer=organizer
        )
        event.save()
        
        # Create RSVP
        rsvp = request.POST.get('rsvp')
        Rsvp.objects.create(rsvp=rsvp, event=event)
        return redirect('home')
    else:
        events = Eventcreation.objects.all()
        rsvps = Rsvp.objects.filter(rsvp__isnull=False)
        rsvps_with_events = [(rsvp, Eventcreation.objects.get(id=rsvp.event.id)) for rsvp in rsvps]
        return render(request, 'home.html', {'events': events, 'rsvps_with_events': rsvps_with_events})

def event_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        time = request.POST.get('time')
        location = request.POST.get('location')
        organizer = request.POST.get('organizer')
        
        event = Eventcreation.objects.create(
            title=title,
            description=description,
            date=date,
            time=time,
            location=location,
            organizer=organizer
        )
        return redirect('event_list')
    return render(request, 'event_create.html')

def event_list(request):
    events = Eventcreation.objects.all()
    return render(request, 'event_list.html', {'events': events})


@login_required(login_url='login')
def rsvp_create(request, event_id):
    event = Eventcreation.objects.get(pk=event_id)
    if request.method == 'POST':
        rsvp = request.POST.get('rsvp')
        rsvp = Rsvp.objects.create(rsvp=rsvp, event=event, user=request.user)
        return redirect('event_list')
    return render(request, 'rsvp.html', {'event': event})
