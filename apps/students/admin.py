from django.contrib import admin
from .models import Student

admin.site.site_header = "LASE"

class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_fname','program', 'id']

admin.site.register(Student, StudentAdmin)