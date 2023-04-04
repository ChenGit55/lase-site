from django.http import Http404
from django.shortcuts import render, redirect
from .models import Student, Statistic
from .forms import StudentForm, StatisticForm
from .utils import superuser_required
from django.contrib import messages

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

@superuser_required
def student_view(request, slug=None):
    students_qs = Student.objects.all() #get a querry set from Student class
    students_list = students_qs
    context = {
        'qs' : students_qs,
        'students' : students_list,
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
        messages.success(request, 'Student enrolled successfully!')
        return redirect('enroll-success')
    return render(request, 'enroll.html', context=context)

def enroll_success_view(request):
    return render(request, 'enroll-success.html', {})

def student_detail_view(request, slug=None):
    form = StatisticForm(request.POST or None)
    if slug is not None:
        try:
            student_detail = Student.objects.get(slug=slug) #get slug if it is not empyt
        except Student.MultipleObjectsReturned:
            student_detail = Student.objects.filter(slug=slug).first()
        except Student.DoesNotExist:
            raise Http404
        except:
            raise Http404
    statistic = Statistic(student_detail)
    context = {
        'sd': student_detail,
        'stats': statistic,
        'form': form,
    }
    return render(request, 'details.html', context=context)