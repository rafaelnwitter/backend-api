from django.db import models
from uuid import uuid4

class Course(models.Model):
    id_course = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    holder_image = models.CharField(max_length=255)
    duration = models.CharField(max_length=5)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.name