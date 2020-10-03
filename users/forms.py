from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class StudentRegisterForm(UserCreationForm):
    email = forms.EmailField()
    department=forms.CharField()
    roll_no=forms.IntegerField()
    course=forms.CharField()
    year=forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'department', 'roll_no', 'course', 'year']


class FacultyRegisterForm(UserCreationForm):
    email = forms.EmailField()
    teacherId=forms.CharField()
    department=forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'teacherId', 'department']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image'] 
