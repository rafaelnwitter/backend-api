# Generated by Django 3.2.9 on 2021-11-23 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
        ('courses', '0001_initial'),
        ('enrollments', '0002_enrollment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='id_course',
        ),
        migrations.AddField(
            model_name='enrollment',
            name='id_course',
            field=models.ManyToManyField(to='courses.Course'),
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='id_student',
        ),
        migrations.AddField(
            model_name='enrollment',
            name='id_student',
            field=models.ManyToManyField(to='students.Student'),
        ),
    ]