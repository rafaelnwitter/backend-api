from rest_framework import serializers
from enrollments import models

class EnrollmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Enrollment
        fields = '__all__'