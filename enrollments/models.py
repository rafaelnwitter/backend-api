from django.db import models
from uuid import uuid4

from students.models import Student
from courses.models import Course

class Enrollment(models.Model):
    id_student = models.OneToOneField(Student, on_delete=models.SET_NULL, null=True)
    id_course =  models.OneToOneField(Course, on_delete=models.SET_NULL, null=True)
    date_enroll = models.DateField()
    date_close = models.DateField()
    score = models.IntegerField()
    status = (
        ("Ap", "Aprovado"),
        ("R", "Reprovado"),
        ("Ad", "Andamento")
    )
