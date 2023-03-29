from django.contrib.auth import authenticate, login, logout, get_user
from django.shortcuts import render, redirect



def home_view(request):

    return render(request, 'home.html', context={})

def camps_view(request):

    return render(request, 'camps.html', context={})

def tournaments_view(request):

    return render(request, 'tournaments.html', context={})

def aboutus_view(request):

    return render(request, 'about-us.html', context={})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username') # get login username
        password = request.POST.get('password') # get login password
        user = authenticate(request, username=username, password=password) # authenticate user
        if user is None:
            context = {'error': 'Invalid username or password!'}
            return render(request, 'login.html', context)
        login(request, user)
        return redirect('/logout', {})

    return render(request, 'login.html', {})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        redirect('/login')
    return render(request, 'logout.html', {})


def register_view(request):

    return render(request, 'register.html', context={})
