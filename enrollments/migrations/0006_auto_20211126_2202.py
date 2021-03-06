# Generated by Django 3.2.9 on 2021-11-26 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
        ('courses', '0001_initial'),
        ('enrollments', '0005_alter_enrollment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.course'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.student'),
        ),
    ]
