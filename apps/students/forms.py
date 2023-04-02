from django import forms
from .models import Student, Statistic

class StudentForm(forms.ModelForm):

    additional_info = forms.CharField(label='Addtional Info', widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 100px;'}))


    class Meta:
        model = Student
        fields = ['student_fname', 'student_lname', 'birth_date', 'gender', 'additional_info']

        labels = {
            'student_fname' : 'Name',
            'student_lname' : 'Last Name',
            'gender' : 'Gender',
            'birth_date' : 'Date of Birth',
        }

        widgets = {
            "birth_date": forms.DateInput(attrs={'type': 'date'})
        }

    def clean(self):
        data = self.cleaned_data
        return data


    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def as_bootstrap(self):
        return self._html_output(
            normal_row='<div class="row"><div class="col">{{label}} {{field}}</div></div>',
            error_row='%s',
            row_ender='</div>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

class StatisticForm(forms.ModelForm):
    class Meta:
        model = Statistic
        fields =['strength', 'speed', 'agility', 'stamina', 'physical']