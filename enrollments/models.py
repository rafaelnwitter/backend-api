from django.db import models
from uuid import uuid4

from students.models import Student
from courses.models import Course

class Enrollment(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, null=False, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)
    date_enroll = models.DateField()
    date_close = models.DateField()
    score = models.IntegerField()
    status_choice = (
        ("Aprovado", "Aprovado"),
        ("Reprovado", "Reprovado"),
        ("Andamento", "Andamento")
    )
    status = models.CharField(max_length=10, choices=status_choice, blank=False, null=False, default="Ad")

    