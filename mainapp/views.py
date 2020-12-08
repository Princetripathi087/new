#import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import *
from .models import login,register
from django.contrib import auth
from django import template
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    if 'login' in request.POST:
        print("login")
        Name = request.POST['Name']
        email = request.POST['email']
        number = request.POST['number']
        passw = request.POST['passw']
        register = auth.authenticate(Name=Name,email=email,number=number,passw=passw)
        if register is not None:
            auth.login(request,register)
            return redirect('index1')
        else:
            messages.info(request,'invalid')
            return redirect('index')
    
    if 'register' in request.POST:
        print("register")
        Name = request.POST['Name']
        print("1")
        email = request.POST['email']
        number = request.POST['number']
        passw = request.POST['passw']
        if register.object.filter(Name==Name).exists():
            messages.info(request,'Name taken')
            return redirect('index')
        elif register.object.filter(email==email).exists():
            messages.info(request,'Email taken')
            return redirect('index')
        else:
            register.object.create(Name=Name,email=email,number=number,passw=passw)
            messages.success(request,'Registeration Done')
    
    return render(request,"index.html")
def index1(request):
    return render(request,'index1.html')
            



