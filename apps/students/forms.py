from django import forms
from .models import Student, Statistic

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_fname', 'student_lname', 'birth_date', 'gender', 'additional_info']

        labels = {
            'student_fname' : 'Name',
            'student_lname' : 'Last Name',
            'birth_date' : 'Date of Birth',
            'gender' : 'Gender',
            'additional_info' : 'Addtional Info'
        }

    def clean(self):
        data = self.cleaned_data
        return data

class StatisticForm(forms.ModelForm):
    class Meta:
        model = Statistic
        fields =['strength', 'speed', 'agility', 'stamina', 'physical']