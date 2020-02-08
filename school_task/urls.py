"""school_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views as user_view
from student import views as student_view
from teacher import views as teacher_view
from classes import views as class_view
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path ('' , user_view.home , name='home-page'),
    path('profile/', user_view.profile , name ='profile'),
    path('classes/', class_view.ClassHome , name ='classes'),
    path('classes/<int:pk>', class_view.ClassStudents , name ='class-students'),
    path('profile/update', user_view.UserUpdateView , name ='profile-update'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name= 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name= 'logout'),
    path('studentDeleteView/<int:pk>',student_view.studentDeleteView.as_view(), name = 'studentDeleteView'),
    path('teacherDeleteView/<int:pk>',teacher_view.teacherDeleteView.as_view(), name = 'teacherDeleteView'),
    path('userUpdate/<int:pk>' , user_view.UserUpdateView, name='user-update'),
    
    path('accounts/',user_view.UserSignUpView,name='user-type'),
    path('studentlist/',student_view.studentlist ,name='students'),
    path('teacherlist/',teacher_view.teacherslist,name='teachers'),

] + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
