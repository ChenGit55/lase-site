from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html', context={})

def aboutus_view(request):
    return render(request, 'about-us.html', context={})

def errors_view(request):
    return render(request, 'error.html', context={})
