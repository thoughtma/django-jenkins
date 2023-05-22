from django import forms
from jenkinsapp.models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'email']
