from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Lecturer, CustomUser
from course.models import Course
from faculty.models import Faculty


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)

class StudentRegistrationForm(forms.Form):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    course = forms.ModelChoiceField(label='course', queryset=Course.objects.all())
    index_number = forms.CharField(label='Index Number', max_length=15)
    phone = forms.CharField(label='Phone Number', max_length=15)
    level = forms.ChoiceField(label='Level', choices=LevelChoices)
    slug = forms.SlugField(max_length=100, unique=True)



class LecturerRegistrationForm(forms.Form):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
    staff_id = forms.CharField(max_length=100, unique=True)
    phone = forms.CharField(max_length=11, unique=True)
    faculty = forms.ModelChoiceField(label='faculty', queryset=Faculty.objects.all())
    slug = forms.SlugField(max_length=100, unique=True)


