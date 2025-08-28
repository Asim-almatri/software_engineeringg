from django.urls import path
from . import views

urlpatterns = [
    path('', views.students_list, name='students_list'),        # قائمة الطلاب
    path('add/', views.student_add, name='student_add'),        # إضافة طالب
    path('<int:pk>/', views.student_detail, name='student_detail'),  # تفاصيل الطالب
    path('edit/<int:pk>/', views.student_edit, name='student_edit'), # تعديل الطالب
    path('delete/<int:pk>/', views.student_delete, name='student_delete'), # حذف الطالب
]
