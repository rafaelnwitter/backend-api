from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from students.api import viewsets as studentviewsets
from courses.api import viewsets as courseviewsets

route = routers.DefaultRouter()

route.register(r'students', studentviewsets.StudentViewSet, basename='Students')
route.register(r'courses', courseviewsets.CourseViewSet, basename='Courses')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('', include(route.urls)),
]
