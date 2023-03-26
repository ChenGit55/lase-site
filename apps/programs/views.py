from django.shortcuts import render
from students.models import Student

# Create your views here.



def programs_view(request):
    students = Student.objects.all()

    context = {
        'sd' : students
    }   

    return render(request, 'programs.html', context)

def lion_cubs_view(request):

    return render(request, 'lion-cubs.html', context={})

def evolution_academy_view(request):

    return render(request, 'evolution-academy.html', context={})

def evolution_futsal_view(request):

    return render(request, 'evolution-futsal-club.html', context={})

def private_training_view(request):

    return render(request, 'private-training.html', context={})

def schools_view(request):

    return render(request, 'schools.html', context={})