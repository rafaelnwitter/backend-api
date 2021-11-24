from django.test import TestCase
from students.models import Student

class StudentTest(TestCase):
    def setUp(self) -> None:
        Student.objects.create(
            name = 'Gustavo Frida',
            nickname = 'guga.frida',
            phone = '48996486598',
            avatar = 'essaehminhafoto.jpg'
        )

    def test_stundet_create(self):
        student_check = Student.objects.get(nickname='guga.frida')
    
    def test_student_delete(self):
        student_checker = Student.objects.exclude(nickname='guga.frida')
