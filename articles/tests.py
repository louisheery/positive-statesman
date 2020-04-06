from django.utils import unittest
from django.test.client import RequestFactory

from .views import article_average

class RequestTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/api/analytics')

        response = article_average(request)

        print(response)

        self.assertEqual(response.status_code, 200)
