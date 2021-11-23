from rest_framework import viewsets
from enrollments.api import serializers
from enrollments import models

class EnrollmentsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EnrollmentsSerializer
    queryset = models.Enrollment.objects.all()