# Generated by Django 3.2.9 on 2021-11-27 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='nickname',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
