from django.http import response
from django.test import TestCase, Client
from .models import *
import io
from rest_framework.parsers import JSONParser
from serializers import StudentSerializer

# Create your tests here.
class DataTest(TestCase):
    def setUp(self):
        student1 = Student.objects.create(
            firstname="First",
             lastname="Student",
             idnumber=100,
             email="first@student.edu",
             schoolyear="FR",
             major="CS",
             gpa="4.0",
             )

        student2 = Student.objects.create(
            firstname="Second",
             lastname="Student",
             idnumber=101,
             email="second@student.edu",
             schoolyear="SR",
             major="ENG",
             gpa="2.0",
             )
        self.test_client = Client()

    def test_student_api(self):
        students_response = self.test_client.get('/regserve/data/students')
        print(f'TEST_STUDENT_API: api response is: {students_response} and the status is {students_response.status_code}')
        self.assertEqual(students_response.status_code, 200)
        print(f'\nTEST_STUDENT_API: api response content is: {students_response.content}')
        student_stream = io.BytesIO(students_response.content)
        print(f'\nTEST_STUDENT_API: api response stream is: {student_stream}')
        student_data = JSONParser().parse(student_stream)
        first_student_data = student_data[0]
        print(f'\nTEST_STUDENT_API: api response data is: {first_student_data} and its ID is {first_student_data["id"]}')
        first_student_db = Student.objects.get(id=student_data['id'])
        print(f'\nTEST_STUDENT_API: api response student object from db is: {first_student_db}')
        
        first_student_serializer = StudentSerializer(first_student_db, data=first_student_data)
        print(f'\nTEST_STUDENT_API: api response student serializer is: {first_student_serializer}')
        print(f'\nTEST_STUDENT_API: api response student serializer validity is: {first_student_serializer.is_valid()}')
        print(f'\nTEST_STUDENT_API: api response student serializer valid data is: {first_student_serializer.validated_data}')
        first_student_api = first_student_serializer.save()
        print(f'\nTEST_STUDENT_API: api response student api object is: {first_student_api}')
        self.assertEqual(first_student_db, first_student_api)

    def test_student(self):
        student_list = Student.objects.all()
        student = student_list[0]
        print(f'Inside test student: student it {student}')
        self.assertEqual(student.id, 1)
        self.assertEqual(student.full_name, 'First Student')
        self.assertEqual(student.idnumber, 100)


class SimpleTest(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_response(self):
        response = self.test_client.get('/regserve')
        print(f'In SimpleTest, response is {response}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Hello world from Django backend!')
