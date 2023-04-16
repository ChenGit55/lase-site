from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def home_view(request):
    return render(request, 'home.html', context={})

def camps_view(request):
    return render(request, 'camps.html', context={})

def tournaments_view(request):
    return render(request, 'tournaments.html', context={})

def aboutus_view(request):
    return render(request, 'about-us.html', context={})

def register_view(request):
    return render(request, 'register.html', context={})
