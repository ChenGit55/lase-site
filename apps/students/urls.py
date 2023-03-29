from django.urls import path
from .views import student_view, student_detail_view, student_create_view ,student_search_view

urlpatterns = [
    path('', student_view, name= 'students'),
    path('details/<slug:slug>', student_detail_view, name='details'),
    path('enroll/', student_create_view, name='enroll'),
    path("search/", student_search_view, name="student-search"),
]