# Generated by Django 3.2.9 on 2021-11-23 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='status',
            field=models.CharField(choices=[('Ap', 'Aprovado'), ('Rp', 'Reprovado'), ('Ad', 'Andamento')], default='Ad', max_length=2),
        ),
    ]
