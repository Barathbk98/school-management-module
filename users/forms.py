from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.db import transaction
from django.forms.utils import ValidationError
from .models import Students, Profile, Teachers
from django.contrib.auth.models import User


class UserSignUpForm(UserCreationForm):
    role = forms.IntegerField()
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email','first_name','last_name', 'password1', 'password2','role']

class StudentUpdateForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        model = Students
        fields = ['image','dob', 'address','father_name','mother_name','gender',]

class TeacherUpdateForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        model = Teachers
        fields = ['image','address', 'gender','dob','phone_no','total_years_of_exp']




# class TeacherSignUpForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.role = 2
#         if commit:
#             user.save()
#         return user


# class StudentSignUpForm(UserCreationForm):
#     # interests = forms.ModelMultipleChoiceField(
#     #     queryset=Subject.objects.all(),
#     #     widget=forms.CheckboxSelectMultiple,
#     #     required=True
#     # )

#     class Meta(UserCreationForm.Meta):
#         model = User

    
#     def save(self):
#         user = super().save(commit=False)
#         user.role = 1
#         user.save()
#         # student = Student.objects.create(user=user)
#         # student.interests.add(*self.cleaned_data.get('interests'))
#         return user
