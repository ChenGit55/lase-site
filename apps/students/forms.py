from django import forms 
from .models import Student

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



class StudentFormOld(forms.Form):
    s_fname = forms.CharField()
    s_lname = forms.CharField()




    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data