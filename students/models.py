from django.db import models
from uuid import uuid4

class Student(models.Model):
    id_student = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=15)
    phone = models.CharField(max_length=12)
    avatar = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)