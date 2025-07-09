"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from school.views import StudentViewSet, CourseViewSet, EnrollmentViewSet, ListEnrollmentPerStudent, ListEnrollmentPerCourse
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'enrollments', EnrollmentViewSet, basename='enrollments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/students/<int:pk>/enrollments/', ListEnrollmentPerStudent.as_view()),
    path('api/coursers/<int:pk>/enrollments/', ListEnrollmentPerCourse.as_view()),
]
