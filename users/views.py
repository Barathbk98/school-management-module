from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.models import User
from .forms import UserSignUpForm , StudentUpdateForm, TeacherUpdateForm
from django.shortcuts import redirect
from .models import Profile , Students, Teachers, Classes
from django.http import HttpResponse,HttpResponseRedirect
import pdb
import os

def home(request):
    return render (request,'users/home.html')

def UserSignUpView(request ):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
        
             form.save(commit=False)
             userObject = form.save(commit=True)
             profile = Profile(user=userObject, role=form.cleaned_data.get('role'))
            #  Profile.objects.create(user=userObject, role=form.cleaned_data.get('role'))
             profile.save()
        return redirect('home-page')
    else:
        form = UserSignUpForm()
    return render(request, 'users/add_user.html', {'form': form})


def profile(request):
    return render(request, 'users/profile.html')


def UserUpdateView(request ,pk ):
    print("afasdfasfasfasdf")
    pdb.set_trace()
    profile = request.user.profile.role
    userid = Students.objects.filter(id = pk).user
    print(userid)
    # if profile == 1:
    #     Student_instance = get_object_or_404(Students , id=pk)
    # elif profile == 2 :
    #     Teacher_instance = get_object_or_404(Teachers,  id=pk)
    # else :
    #     print('passed for 1')

    if profile == 1 or 3:
        form = StudentUpdateForm(request.POST)
    elif profile == 2 or 3 :
        form = TeacherUpdateForm(request.POST)
    else:
        print("passed for 2")

    if request.method == 'POST':
        if form.is_valid():
            if profile == 1 or 3:
                StudentData = Students.objects.get(user=request.user)
                student=form.save(commit=False)
                student.user= pk
                student.profile = StudentData.profile
                print("testasdfasdf")
                pdb.set_trace()
                student.standard = StudentData.standard
                student.save()
                pdb.set_trace()
                print(student)
            elif profile == 2 or 3:
                TeacherData = Teachers.objects.get(user=request.user)
                teacher = form.save(commit=False)
                #teacher.user = request.user
                teacher.profile = request.user.profile
                teacher.standard = TeacherData.standard
                teacher.save(commit=True)
                print(teacher)
            else:
                print('passed for 3')
        else:
            pass

        return redirect('profile')
    else:
        if profile == 1 or 3:
            form = StudentUpdateForm(instance = get_object_or_404(Students , id=pk))
            return render(request, 'students/students_form.html', {'form': form})
        elif profile == 2 or 3:
            form = TeacherUpdateForm(instance= get_object_or_404(Teachers,  id=pk))
            return render(request, 'teachers/teachers_form.html', {'form': form})
        else:
            return render(request, 'users/home.html')

