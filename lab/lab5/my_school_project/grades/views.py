from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Grade
from .forms import GradeForm

def grades_list(request):
    """
    يعرض قائمة بجميع الدرجات مع إمكانية البحث
    """
    grades = Grade.objects.all().select_related('student', 'course')
    query = request.GET.get('q')
    if query:
        grades = grades.filter(
            Q(student__name__icontains=query) |
            Q(course__name__icontains=query)
        )
    context = {'grades': grades}
    return render(request, 'grades/grades_list.html', context)

def add_grade(request):
    """
    يعالج نموذج إضافة درجة جديدة
    """
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grades_list')
    else:
        form = GradeForm()
    return render(request, 'grades/grade_form.html', {'form': form, 'title': 'إضافة درجة'})

def grade_detail(request, pk):
    """
    يعرض تفاصيل درجة معينة
    """
    grade = get_object_or_404(Grade, pk=pk)
    return render(request, 'grades/grade_detail.html', {'grade': grade})

def grade_edit(request, pk):
    """
    يعالج نموذج تعديل درجة
    """
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grades_list')
    else:
        form = GradeForm(instance=grade)
    return render(request, 'grades/grade_form.html', {'form': form, 'title': 'تعديل درجة'})

def grade_delete(request, pk):
    """
    يحذف درجة من قاعدة البيانات
    """
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == 'POST':
        grade.delete()
        return redirect('grades_list')
    return render(request, 'grades/grade_confirm_delete.html', {'grade': grade})
