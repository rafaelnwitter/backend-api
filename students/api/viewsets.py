from rest_framework import viewsets
from students.api import serializers
from students import models

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()