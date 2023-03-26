from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

# Create your views here.

def student_search_view(request):
    query = request.GET.get("q") #get the input text by the name
    student_detail = None
    if query is not None:        
        student_detail = Student.objects.filter(slug__icontains= query)
           
    context = {
        'student' : student_detail,
        'qerry' : query
    }

    return render(request, 'student-search.html', context )

@login_required
def student_view(request):

    students_qs = Student.objects.all() #get a querry set from Student class

    students_list = students_qs

    context = {
        'qs' : students_qs,
        'students': students_list,
    }
    return render(request, 'students.html', context= context)

def student_create_view(request):
    form = StudentForm(request.POST or None)
    context= {
        'form': form
    }
    if form.is_valid():
        student = form.save()
        context['form'] = StudentForm() #reinitializing form
        return redirect(student.get_absolute_url())

    return render(request, 'enroll.html', context=context)


def student_detail_view(request, slug=None):
    
    if slug is not None:
        try:
            student_detail = Student.objects.get(slug=slug) #get slug if it is not empyt
        except Student.MultipleObjectsReturned:
            student_detail = Student.objects.filter(slug=slug).first() 
        except Student.DoesNotExist:
            raise Http404
        except:
            raise Http404

    context = {
        'sd': student_detail
    }
    return render(request, 'details.html', context=context)