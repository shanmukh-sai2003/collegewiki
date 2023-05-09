from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *

# Create your views here.
#handles home page
def index(request):
    if request.method == "POST":
        search = request.POST["search"]
        if Entry.objects.filter(title = search):
            url = search + "/"
            return redirect(url)
        else:
            return render(request, 'pedia/index.html', {
                "pedias": Entry.objects.all(),
                "message": "no match found try for another title",
                "logged": request.user.is_authenticated
            })
        
    if request.user.is_authenticated:
        return render(request, "pedia/index.html", {
            "pedias": Entry.objects.all(),
            "logged": True
        })
    
    return render(request, "pedia/index.html", {
        "pedias": Entry.objects.all(),
        "logged": False
    })

#handles full page
def fullPage(request, name):
    return render(request, "pedia/fullpage.html", {
        "entry": Entry.objects.get(title = name),
        "logged": request.user.is_authenticated
    })

#handles add page
def add(request):
    if request.method == "POST":
        title = request.POST["title"]
        body = request.POST["body"]

        if Entry.objects.filter(title = title):
            return render(request, 'pedia/add.html', {
                "message" : "this title already exsist please try another name",
                "title": title,
                "body": body,
                "logged": request.user.is_authenticated
            })
        
        newEntry = Entry.objects.create(userName = request.user.username, title = title, body = body)
        newEntry.save()
        url = title + "/"
        return redirect(url)
    if request.user.is_authenticated:
        return render(request, 'pedia/add.html', {
            "logged": request.user.is_authenticated
        })
    else:
        return render(request, 'pedia/login.html', {
            "message": "please login to add new Note"
        })
    

#handles login page
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, "pedia/login.html", {
                "message": "invaild cerdintails, Try again"
            })

    return render(request, "pedia/login.html")

#handles logout page
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

#handle signup page
def signup(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        pass1 = request.POST["password1"]
        pass2 = request.POST["password2"]

        if pass1 != pass2:
            return render(request, 'pedia/register.html', {
                "message" : "passwords didn't match"
            })
        
        if User.objects.filter(username = email) :
            return render(request, 'pedia/register.html', {
                "message" : "email already registered"
            })
        
        newUser = User.objects.create_user(email, email, pass1)
        newUser.first_name = firstname
        newUser.last_name = lastname
        newUser.email = email
        newUser.save()

        return render(request, 'pedia/login.html', {
            "message" : "Successfully Registered"
        })

    return render(request, 'pedia/register.html')

