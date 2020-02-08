from users.models import Students
from django.contrib.auth.models import User
from django.forms import ModelForm


class StudentDetailForm(ModelForm):
     class Meta:
         model = Students
         exclude = [ 'profile','standards']