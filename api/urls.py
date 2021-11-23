from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from students.api import viewsets as studentviewsets
from courses.api import viewsets as courseviewsets
from enrollments.api import viewsets as enrollmentviewsets

route = routers.DefaultRouter()

route.register(r'students', studentviewsets.StudentViewSet, basename='Students')
route.register(r'courses', courseviewsets.CourseViewSet, basename='Courses')
route.register(r'enrollments', enrollmentviewsets.EnrollmentsViewSet, basename='Enrollments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('', include(route.urls)),
    path('', include(route.urls)),
]
