
from django.test import TestCase
from enrollments.models import Enrollment
from courses.models import Course
from students.models import Student
class EnrollmentTest(TestCase):
    def setUp(self) -> None:
        Enrollment.objects.create(
            student = Student.objects.create(
            name = 'Gustavo Frida',
            nickname = 'guga.frida',
            phone = '48996486598',
            avatar = 'essaehminhafoto.jpg'
        ),
            course = Course.objects.create(
                name='',
                description='',
                holder_image='',
                duration=''
            ),
            date_enroll = '2021-11-23',
            date_close = '2021-12-23',
            score = 10,
            status = 'Aprovado'
        )

    def test_enrollment(self):
        enrollment_check = Enrollment.objects.get(status='Aprovado')
        self.assertEquals(enrollment_check.status, "Aprovado")
    
    def test_enrollment_student(self):
        enrollment_check = Enrollment.objects.get(status='Aprovado')
        self.assertEquals(enrollment_check.student.name, "Gustavo Frida")