from django.shortcuts import render
from django.http import HttpResponse
from users.models import Classes,Students
from django.contrib.auth.models import User
from users.models import Students,Profile, Teachers

def ClassHome(request):
    context = {
        'classes': Classes.objects.all(),
    }
    return render (request , 'classes/classeshome.html' , context)

def ClassStudents(request, pk):
    #student = User.objects.get(role = 1)
    context = {
        'students' : Students.objects.filter(standard = pk)
        
    }
    return render (request , 'classes/classstudentslist.html', context)
