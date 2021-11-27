from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from enrollments.api import serializers
from enrollments import models

class EnrollmentsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EnrollmentsSerializer
    queryset = models.Enrollment.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['status', 'date_enroll', 'score', 'student', 'course']
    search_fields = ['status', 'date_enroll', 'score', 'student', 'course']