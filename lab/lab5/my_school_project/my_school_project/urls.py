# school_management_project/urls.py
# هذا هو ملف الروابط الرئيسي الذي يربط جميع التطبيقات

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('teachers/', include('teachers.urls')),
    path('students/', include('students.urls')),
    path('courses/', include('courses.urls')),
     
    path('grades/', include('grades.urls')), # إضافة مسارات الدرجات
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

