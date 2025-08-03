from django.urls import path
from . import views

# Register the app namespace for reverse URL resolution
app_name = 'page'

urlpatterns = [
    path('', views.index, name='index'),

    # Add URL patterns for student operations
    path('students/', views.students_list, name='students_list'),
    path('students/add/', views.student_add, name='student_add'),
    path('students/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),

    # Add URL patterns for 'one', 'two', and 'three'
    path('one/', views.one, name='one'),
    path('two/', views.two, name='two'),
    path('three/', views.three, name='three'),

    # Add URL patterns for course operations
    path('courses/', views.courses_list, name='courses_list'),
    path('courses/add/', views.course_add, name='course_add'),
    path('courses/<int:pk>/edit/', views.course_edit, name='course_edit'),
    path('courses/<int:pk>/delete/', views.course_delete, name='course_delete'),

    # Include other URL patterns if needed
    # path('other/', include('other_app.urls')),
]
