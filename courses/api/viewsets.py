from rest_framework import viewsets
from courses.api import serializers
from courses import models

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CourseSerializer
    queryset = models.Course.objects.all()