from django.urls import path
from . import views

urlpatterns = [
    path('', views.grades_list, name='grades_list'),
    path('add/', views.add_grade, name='add_grade'),
    path('<int:pk>/', views.grade_detail, name='grade_detail'),
    path('edit/<int:pk>/', views.grade_edit, name='grade_edit'),
    path('delete/<int:pk>/', views.grade_delete, name='grade_delete'),
]

