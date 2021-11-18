from django.http import response
from django.test import TestCase, Client

# Create your tests here.
class SimpleTest(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_response(self):
        response = self.test_client.get('/regserve')
        print(f'In SimpleTest, response is {response}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Hello world from Django backend!')
