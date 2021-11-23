from django.db import models
from uuid import uuid4

from students.models import Student
from courses.models import Course

class Enrollment(models.Model):
    id_student = models.ManyToManyField(Student)
    id_course =  models.OneToOneField(Course, on_delete=models.SET_NULL, null=True)
    date_enroll = models.DateField()
    date_close = models.DateField()
    score = models.IntegerField()
    status_choice = (
        ("Ap", "Aprovado"),
        ("Rp", "Reprovado"),
        ("Ad", "Andamento")
    )
    status = models.CharField(max_length=2, choices=status_choice, blank=False, null=False, default="Ad")
