# grades/models.py
from django.db import models
from students.models import Student
from courses.models import Course
from django.utils import timezone

class Grade(models.Model):
    """
    نموذج يمثل درجة طالب في دورة.
    """
    # تم تحديث الحقول هنا لإضافة related_name لمنع التضارب
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades_app_grades', verbose_name="الطالب")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='grades_app_grades', verbose_name="الدورة")
    GRADE_CHOICES = [
        ('midterm', 'منتصف الفصل'),
        ('final', 'نهائي'),
        ('quiz', 'اختبار قصير'),
        ('homework', 'واجب منزلي'),
    ]
    grade_type = models.CharField(max_length=20, choices=GRADE_CHOICES, verbose_name="نوع الدرجة")
    grade = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="الدرجة")
    # تم تعديل هذا الحقل ليسمح بالقيم الفارغة مؤقتًا لحل مشكلة الهجرة
    date_given = models.DateField(null=True, blank=True, verbose_name="تاريخ إعطاء الدرجة")

    class Meta:
        verbose_name = "درجة"
        verbose_name_plural = "درجات"
        unique_together = ('student', 'course', 'grade_type')

    def __str__(self):
        return f'{self.student.first_name} - {self.course.title} ({self.get_grade_type_display()})'
