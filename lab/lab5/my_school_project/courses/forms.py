# courses/forms.py
from django import forms
from .models import Course, Enrollment, Grade

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'code', 'teacher', 'description']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']

# نموذج لإضافة الدرجات
class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'course', 'grade_type', 'grade']
