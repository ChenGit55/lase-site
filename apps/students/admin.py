from django.contrib import admin
from .models import Student, Statistic

admin.site.site_header = "LASE"

class StudentAdmin(admin.ModelAdmin):
    list_display = ['fname','program', 'id']

admin.site.register(Student, StudentAdmin)

class StatisticAdmin(admin.ModelAdmin):
    list_display= ['student', 'strength', 'speed', 'agility', 'stamina', 'physical']

admin.site.register(Statistic, StatisticAdmin)