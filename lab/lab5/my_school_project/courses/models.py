# courses/models.py
from django.db import models
from students.models import Student
from teachers.models import Teacher

class Course(models.Model):
    """
    نموذج يمثل دورة دراسية.
    """
    title = models.CharField(max_length=200, verbose_name="عنوان الدورة")
    code = models.CharField(max_length=50, unique=True, verbose_name="كود الدورة")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="المعلم")
    description = models.TextField(verbose_name="الوصف")
    
    class Meta:
        verbose_name = "دورة"
        verbose_name_plural = "دورات"

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    """
    نموذج يمثل تسجيل طالب في دورة دراسية.
    """
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="الطالب")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="الدورة")
    enrollment_date = models.DateField(auto_now_add=True, verbose_name="تاريخ التسجيل")

    class Meta:
        verbose_name = "تسجيل"
        verbose_name_plural = "تسجيلات"
        unique_together = ('student', 'course')

    def __str__(self):
        return f'{self.student.first_name} في {self.course.title}'

class Grade(models.Model):
    """
    نموذج يمثل درجة طالب في دورة.
    """
    # تم تحديث الحقول هنا لإضافة related_name لمنع التضارب
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='course_grades', verbose_name="الطالب")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_grades', verbose_name="الدورة")
    GRADE_CHOICES = [
        ('midterm', 'منتصف الفصل'),
        ('final', 'نهائي'),
        ('quiz', 'اختبار قصير'),
        ('homework', 'واجب منزلي'),
    ]
    grade_type = models.CharField(max_length=20, choices=GRADE_CHOICES, verbose_name="نوع الدرجة")
    grade = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="الدرجة")
    
    class Meta:
        verbose_name = "درجة"
        verbose_name_plural = "درجات"
        unique_together = ('student', 'course', 'grade_type')

    def __str__(self):
        return f'{self.student.first_name} - {self.course.title} ({self.get_grade_type_display()})'

