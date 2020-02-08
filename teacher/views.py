from django.shortcuts import render
from django.views.generic import CreateView
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import Teachers
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from users.models import Profile , Teachers
from django.contrib.auth.models import User



@login_required

def teacherslist(request):
    context = {
        'teachers':Teachers.objects.all(),
    }
    return render(request, 'teachers/teacherslist.html', context)

class teacherDeleteView(DeleteView):
    model = User
    template_name = 'teachers/teachers_deletion.html'
    success_url = reverse_lazy('teachers')
    