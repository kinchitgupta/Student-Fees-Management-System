"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from App1.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('adminreg/',adminreg),
    path('showadmins/',showadmins),
    path('accountant_reg/',accountant_reg),
    path('accountant_reg2/',accountant_reg2),
    path('coursereg/',coursereg),
    path('show_course/',show_course),
    path('show_course1/',show_course1),
    path('edit_course/',edit_course),
    path('edit_course1/',edit_course1),
    path('studentreg/',studentreg),
    path('accountant_show/',accountant_show),
    path('show_student/',show_student),
    path('student_view/',student_view),
    path('edit_accountant/',edit_accountant),
    path('edit_accountant1/',edit_accountant1),
    path('edit_student/',edit_student),
    path('edit_student1/',edit_student1),
    path('delete_accountant/',delete_accountant),
    path('delete_accountant1/',delete_accountant1),
    path('change_accountant_password/',change_accountant_password),
    path('change_accountant_password1/',change_accountant_password1),
    path('del_student/',del_student),
    path('del_student1/',del_student1),
    path('del_course/',del_course),
    path('del_course1/',del_course1),
    path('change_student_password/',change_student_password),
    path('change_student_password1/',change_student_password1),
    path('student_course/',student_course),
    path('edit_studentcourse/',edit_studentcourse),
    path('edit_studentcourse1/',edit_studentcourse1),
    path('del_studentcourse/',del_studentcourse),
    path('del_studentcourse1/',del_studentcourse1),
    path('studentcourse_reg/',studentcourse_reg),
    path('edit_adminprofile/',edit_adminprofile),
    path('edit_adminprofile1/',edit_adminprofile1),
    path('edit_accountantprofile/',edit_accountantprofile),
    path('edit_accountantprofile1/',edit_accountantprofile1),
    path('pay/',pay),
    path('fees_transitions/',fees_transitions),
    path('download_fees_pdf/',download_fees_pdf),
    path('edit_fees/',edit_fees),
    path('edit_fees1/',edit_fees1),
    path('del_fees/',del_fees),
    path('del_fees1/',del_fees1),
    path('login/',login),
    path('logout/',logout),
    path('adminhome/',adminhome),
    path('accountanthome/',accountanthome),
    path('studenthome/',studenthome),
    path('uploadphoto/',uploadphoto),
    path('autherror/',autherror),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
