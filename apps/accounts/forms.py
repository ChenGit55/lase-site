from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    date_joined = forms.DateField(required=False)

    class Meta(UserChangeForm.Meta):
        model = get_user_model()

    def clean(self):
        #original values
        cleaned_data = super().clean()
        cleaned_data.pop('is_superuser', None)
        cleaned_data.pop('is_active', None)
        cleaned_data.pop('is_staff', None)
        return cleaned_data
