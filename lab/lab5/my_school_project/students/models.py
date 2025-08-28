from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='الاسم')
    student_id = models.CharField(max_length=20, unique=True, verbose_name='الرقم الأكاديمي')
    email = models.EmailField(unique=True, verbose_name='البريد الإلكتروني')
    phone = models.CharField(max_length=20, blank=True, verbose_name='رقم الهاتف')
    photo = models.ImageField(upload_to='students_photos/', blank=True, null=True, verbose_name='صورة')

    class Meta:
        verbose_name = "طالب"
        verbose_name_plural = "الطلاب"

    def __str__(self):
        return self.name