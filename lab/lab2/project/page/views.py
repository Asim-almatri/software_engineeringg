from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course
from .forms import StudentForm, CourseForm

# Create your views here.
def index(request):
    return render(request, 'page/index.html', {'name': 'asim almatri', 'size': 20792727917, 'country': 'yemen', 'city': 'sana\'a'})

def one(request):
    # ميزة: فلترة وعكس الكلمات في نص يُدخله المستخدم
    from .models import Course
    courses = Course.objects.all()
    result = None
    text = request.GET.get('text', '')
    if text:
        words = text.split()
        filtered = [w for w in words if len(w) > 2]
        reversed_words = [w[::-1] for w in filtered]
        result = ' '.join(reversed_words)
    return render(request, 'page/one.html', {'result': result, 'text': text, 'courses': courses})

def two(request):
    # ميزة: فلترة وعكس الكلمات في نص يُدخله المستخدم
    result = None
    text = request.GET.get('text', '')
    if text:
        words = text.split()
        filtered = [w for w in words if w.lower() != w[::-1].lower()]
        reversed_words = [w[::-1] for w in filtered]
        result = ' '.join(reversed_words)
    return render(request, 'page/two.html', {'result': result, 'text': text})

def three(request):
    # إعادة توجيه صفحة three لعرض الطلاب من قاعدة البيانات
    return students_list(request)

def students_list(request):
    students = Student.objects.all()
    # حساب المعدل
    grades_map = {'A+': 100, 'A': 95, 'A-': 90, 'B+': 85, 'B': 80, 'B-': 75, 'C+': 70, 'C': 65, 'C-': 60, 'D': 50, 'F': 0}
    total = 0
    count = 0
    for s in students:
        val = grades_map.get(s.grade.upper(), None)
        if val is not None:
            total += val
            count += 1
    avg = total / count if count else None
    from .models import Course
    courses = Course.objects.all()
    return render(request, 'page/three.html', {'students': students, 'avg': avg, 'courses': courses})

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('page:students_list')
    else:
        form = StudentForm()
    return render(request, 'page/student_form.html', {'form': form, 'action': 'Add'})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('page:students_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'page/student_form.html', {'form': form, 'action': 'Edit'})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('page:students_list')
    return render(request, 'page/student_confirm_delete.html', {'student': student})

def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'page/courses.html', {'courses': courses})

def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page:courses_list')
    else:
        form = CourseForm()
    return render(request, 'page/course_form.html', {'form': form, 'action': 'Add'})

def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('page:courses_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'page/course_form.html', {'form': form, 'action': 'Edit'})

def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('page:courses_list')
    return render(request, 'page/course_confirm_delete.html', {'course': course})