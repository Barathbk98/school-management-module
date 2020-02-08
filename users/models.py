from django.db import models    
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Classes(models.Model):
    standard = models.TextField( max_length= 10 )
    
    def __str__(self):
        return self.standard


class Profile(models.Model):
    STUDENT = 1
    TEACHER = 2
    SUPERVISOR = 3
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (SUPERVISOR, 'Supervisor'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def __str__(self):
        return str(self.role)

class Students(models.Model):
    user= models.OneToOneField(User, default = None, on_delete=models.CASCADE)

    profile = models.ForeignKey(Profile, null=True ,on_delete=models.CASCADE)

    standard = models.ForeignKey(Classes , on_delete=models.CASCADE)

    image =  models.ImageField(upload_to= 'students_profile_pics',default= 'default.jpg',)

    father_name = models.CharField(max_length=200, null=True)

    mother_name = models.CharField(max_length=200, null=True)
    
    address = models.CharField(max_length=200, null=True)

    phone_no = models.CharField(max_length=10, null=True)
    
    dob = models.DateField(max_length=10,help_text="format : YYYY-MM-DD",null=True)
    
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    
    gender = models.CharField(choices=gender_choices,max_length=1,default=None,null=True)
    
    
    def __str__(self):
        return str(self.user.username)
    
    
class Teachers(models.Model):

    #classes = models.ForeignKey(classes, default = None, null = True,on_delete=models.CASCADE)
    user= models.OneToOneField(User, default = None, on_delete=models.CASCADE)

    profile = models.ForeignKey(Profile, default = None, null=True ,on_delete=models.CASCADE)

    standard = models.ManyToManyField(Classes)

    image =  models.ImageField(upload_to= 'teachers_profile_pics',default= 'default.jpg',height_field='122' , width_field='122')

    address = models.CharField(max_length=200, null=True)

    phone_no = models.CharField(max_length=10, null=True)
    
    dob = models.DateField(max_length=10,help_text="format : YYYY-MM-DD",null=True)
    
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    
    gender = models.CharField(choices=gender_choices,max_length=1,default=None,null=True)

    total_years_of_exp = models.IntegerField()

    # class_choices = [('1st','1st'),('2nd','2nd'),('3rd','3rd'),('4th','4th'),('5th','5th')]

    # standard = models.CharField(choices= class_choices,max_length=5,default=None,null=True)

    def __str__(self):
        return str(self.user.username)