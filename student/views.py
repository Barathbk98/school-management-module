from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from users.models import Students
from django.contrib.auth.models import User
from users.models import Profile
from django.views.generic import CreateView, UpdateView, DeleteView



@login_required()
def studentlist(request):
    context = {
        'Students':Students.objects.all(),
    }
    return render (request,'students/studentslist.html', context)


class UpdateStudent(CreateView):
    model = Students
    template_name = 'students/students_form.html'
    fields = ['father_name','mother_name','address','phone_no','dob','gender','standard']

    def form_valid(self, form):
 
        model = form.save(commit=False)
        model.submitted_by = self.request.user
        Students.profile = 1
        model.save()
        return HttpResponseRedirect(reverse('students'))

class studentDeleteView(DeleteView):
    model = User
    template_name = 'students/students_deletion.html'
    success_url = reverse_lazy('students')

