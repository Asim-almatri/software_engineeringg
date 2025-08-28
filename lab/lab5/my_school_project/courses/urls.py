from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.courses_list, name='courses_list'),
    path('add/', views.add_course, name='add_course'),
    path('<int:pk>/', views.course_detail, name='course_detail'),
    path('edit/<int:pk>/', views.course_edit, name='course_edit'),
    path('delete/<int:pk>/', views.course_delete, name='course_delete'),
]

