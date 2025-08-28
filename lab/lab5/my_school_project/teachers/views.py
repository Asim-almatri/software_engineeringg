# teachers/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Teacher
from .forms import TeacherForm

def teachers_list(request):
    query = request.GET.get('q')
    teachers = Teacher.objects.all()
    if query:
        teachers = teachers.filter(
            Q(name__icontains=query) |
            Q(specialty__icontains=query)
        )
    return render(request, 'teachers/teachers_list.html', {'teachers': teachers})

def teacher_add(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers_list')
    else:
        form = TeacherForm()
    return render(request, 'teachers/teacher_form.html', {'form': form, 'page_title': 'إضافة معلم'})

def teacher_edit(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teachers_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'teachers/teacher_form.html', {'form': form, 'page_title': 'تعديل بيانات معلم'})

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teachers_list')
    return render(request, 'teachers/teacher_confirm_delete.html', {'teacher': teacher})

