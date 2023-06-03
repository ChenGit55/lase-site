from django.urls import path
from .views import (
    student_view,
    student_detail_view,
    student_edit_view,
    student_create_view,
    student_search_view,
    enroll_success_view,
)

urlpatterns = [
    path('', student_view, name= 'students'),
    path('details/<slug:slug>', student_detail_view, name='details'),
    path('edit/<slug:slug>', student_edit_view, name='edit'),
    path('enroll/', student_create_view, name='enroll'),
    path('enroll-success/', enroll_success_view, name='enroll-success'),
    path("search/", student_search_view, name="student-search"),
]