from django.db import models
from uuid import uuid4

from students.models import Student
from courses.models import Course

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    date_enroll = models.DateField()
    date_close = models.DateField()
    score = models.IntegerField()
    status_choice = (
        ("Aprovado", "Aprovado"),
        ("Reprovado", "Reprovado"),
        ("Andamento", "Andamento")
    )
    status = models.CharField(max_length=10, choices=status_choice, blank=False, null=False, default="Ad")

    def id_student(id):
        id_student = id

    def id_course(id):
        id_course = id
