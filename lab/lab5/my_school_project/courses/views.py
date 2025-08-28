# courses/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Course, Enrollment, Grade
from .forms import CourseForm, EnrollmentForm, GradeForm # استيراد النماذج من forms.py

def courses_list(request):
    """
    يعرض قائمة بجميع الدورات.
    """
    courses = Course.objects.all()
    return render(request, 'courses/courses_list.html', {'courses': courses})

def course_detail(request, pk):
    """
    يعرض تفاصيل دورة محددة.
    """
    course = get_object_or_404(Course, pk=pk)
    enrollments = Enrollment.objects.filter(course=course)
    context = {
        'course': course,
        'enrollments': enrollments,
    }
    return render(request, 'courses/course_detail.html', context)

def add_course(request):
    """
    يعالج إضافة دورة جديدة.
    """
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('courses:courses_list'))
    else:
        form = CourseForm()
    return render(request, 'courses/add_course.html', {'form': form})

def enroll_form(request):
    """
    يعالج إضافة تسجيل جديد (طالب في دورة).
    """
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('courses:courses_list'))
    else:
        form = EnrollmentForm()
    return render(request, 'courses/enroll_form.html', {'form': form})


def course_delete(request, pk):
    """
    يعالج حذف دورة.
    """
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect(reverse('courses:courses_list'))
    return render(request, 'courses/course_confirm_delete.html', {'course': course})

def course_edit(request, pk):
    """
    يعالج تعديل دورة.
    """
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect(reverse('courses:courses_list'))
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/course_edit.html', {'form': form})
