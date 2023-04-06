from django import forms
from .models import Student, Statistic

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['student_fname', 'student_lname', 'birth_date', 'gender', 'program', 'additional_info']

        labels = {
            'student_fname' : 'Name',
            'student_lname' : 'Last Name',
            'gender' : 'Gender',
            'birth_date' : 'Date of Birth',
            'additional_info' : 'Addtional Info',
        }

        widgets = {
            "birth_date": forms.DateInput(attrs={'type': 'date'}),
            "additional_info" : forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 100px;'}),
        }

    def clean(self):
        data = self.cleaned_data
        return data

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class FiltroForm(forms.Form):
    full_name = forms.CharField(required=False)
    age = forms.CharField(required=False)
    program = forms.CharField(required=False)

class StatisticForm(forms.ModelForm):
    class Meta:
        model = Statistic
        fields = ['strength', 'speed', 'agility', 'stamina', 'physical']
