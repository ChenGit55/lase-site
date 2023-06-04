from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserChangeForm
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib import messages
from students.models import Student

User = get_user_model()

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username') # get login username
        password = request.POST.get('password') # get login password
        user = authenticate(request, username=username, password=password) # authenticate user
        if user is None:
            context = {'error': 'Invalid username or password!'}
            return render(request, 'login.html', context)
        login(request, user)
        return redirect(reverse_lazy(settings.LOGIN_REDIRECT_URL, args=[request.user.id])) #redirect to profile page, after login
    return render(request, 'login.html', {})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        redirect('/login')
    return render(request, 'logout.html', {})

def create_user_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_superuser = True
            user.save()
            messages.success(request, 'User successfully registered!')
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
        'form_errors': form.errors,
    }
    return render(request, 'sign-up.html', context)

@login_required
def profile_view(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    students = Student.objects.filter(user=user)
    context = {
        'user': user,
        'students': students
    }
    return render(request, 'profile.html', context)

@login_required
def edit_profile_view(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            print(form.errors)
            form.save()
            return redirect(reverse_lazy(settings.LOGIN_REDIRECT_URL, args=[request.user.id]))
        else:
            print(form.errors)
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'edit-profile.html', {'form': form})