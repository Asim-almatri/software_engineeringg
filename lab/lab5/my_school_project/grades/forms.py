# grades/forms.py
from django import forms
from .models import Grade

class GradeForm(forms.ModelForm):
    """
    نموذج (Form) لإضافة درجات الطلاب.
    يتأكد من أن حقول النموذج تتطابق مع حقول Grade Model.
    """
    class Meta:
        model = Grade
        # تم تصحيح الحقول لتتطابق مع نموذج Grade في models.py
        fields = ['student', 'course', 'grade_type', 'grade']
