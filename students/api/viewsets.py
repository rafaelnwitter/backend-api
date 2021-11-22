from rest_framework import viewssets
from students.api import serializers
from students import models

class StudentViewSet(viewssets.ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = models.Stundet.objects.all()