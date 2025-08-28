# courses/admin.py
from django.contrib import admin
from .models import Course, Enrollment, Grade

admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Grade)
