from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from students.api import viewsets as studentviewsets
from courses.api import viewsets as courseviewsets
from enrollments.api import viewsets as enrollmentviewsets

route = routers.DefaultRouter()

route.register(r'students', studentviewsets.StudentViewSet, basename='Students')
route.register(r'courses', courseviewsets.CourseViewSet, basename='Courses')
route.register(r'enrollments', enrollmentviewsets.EnrollmentsViewSet, basename='Enrollments')

schema_view = get_schema_view(
   openapi.Info(
      title="Management API for colleges",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('', include(route.urls)),
    path('', include(route.urls)),
]
