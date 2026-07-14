from django.contrib import admin
from django.contrib.auth.models import User

from .models import *

admin.site.register(AdminData)
admin.site.register(LoginData)
admin.site.register(AccountantData)
admin.site.register(StudentData)
admin.site.register(CourseData)
admin.site.register(StudentCourse)
admin.site.register(FeesData)
admin.site.register(PhotosData)
