# students/views.py
import os
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import Student
from .forms import StudentForm
from django.db.models import Q
from courses.models import Enrollment # استيراد نموذج Enrollment

def students_list(request):
    """
    يعرض قائمة بجميع الطلاب مع إمكانية البحث
    """
    query = request.GET.get('q')
    if query:
        # البحث في الاسم أو الرقم الأكاديمي
        students = Student.objects.filter(Q(name__icontains=query) | Q(student_id__icontains=query))
    else:
        students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students/students_list.html', context)

def student_add(request):
    """
    يعالج نموذج إضافة طالب جديد مع صورة
    """
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form, 'title': 'إضافة طالب'})

def student_detail(request, pk):
    """
    يعرض تفاصيل طالب معين والدورات التي سجل فيها.
    """
    student = get_object_or_404(Student, pk=pk)
    # جلب جميع تسجيلات الطالب
    enrolled_courses = Enrollment.objects.filter(student=student)
    
    # تمرير المتغير إلى القالب
    return render(request, 'students/student_detail.html', {'student': student, 'enrolled_courses': enrolled_courses})

def student_edit(request, pk):
    """
    يعالج نموذج تعديل بيانات طالب مع صورة
    """
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            # حفظ الصورة القديمة
            old_photo = student.photo.path if student.photo else None
            
            # حفظ النموذج
            form.save()
            
            # إذا تم رفع صورة جديدة، احذف الصورة القديمة
            if form.cleaned_data.get('photo') and old_photo and os.path.exists(old_photo):
                os.remove(old_photo)
                
            return redirect('students_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form, 'title': 'تعديل طالب'})

def student_delete(request, pk):
    """
    يحذف طالبًا من قاعدة البيانات ويحذف صورته
    """
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        # حذف الصورة من نظام الملفات قبل حذف الكائن
        if student.photo and os.path.exists(student.photo.path):
            os.remove(student.photo.path)
            
        student.delete()
        return redirect('students_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})
