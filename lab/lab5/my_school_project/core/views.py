# core/views.py
# عرض لوحة التحكم الرئيسية
from django.shortcuts import render
from students.models import Student
from teachers.models import Teacher
from courses.models import Course
from grades.models import Grade # استيراد نموذج الدرجات

def dashboard_view(request):
    """
    يعرض لوحة التحكم الرئيسية مع ملخصات الأعداد
    """
    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()
    total_courses = Course.objects.count()
    total_grades = Grade.objects.count() # إضافة عدد الدرجات
    
    context = {
        'total_students': total_students,
        'total_teachers': total_teachers,
        'total_courses': total_courses,
        'total_grades': total_grades, # إضافته إلى السياق
    }
    return render(request, 'core/dashboard.html', context)