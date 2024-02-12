from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from rest_framework.test import APIClient
import pyshorteners

class TestShortenedURL(TestCase):
    def setUp(self):
        # Create a test client
        self.client = APIClient()
        original_url = 'http://example.com'
        shortened_url = pyshorteners.Shortener().tinyurl.short(original_url)
        self.original_url = original_url
        self.shortened_url = shortened_url

    def test_ShortenedURLAPIView(self):
        # Create a shortened URL
        url_data = {'original_url': self.original_url}
        response = self.client.post('/url_shortener/', url_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['shortened_url'], self.shortened_url)

    def test_OriginalURLAPIView(self):
        # First, create a shortened URL
        url_data = {'original_url': self.original_url}
        self.client.post('/url_shortener/', url_data, format='json')

        # Now, get the original URL from the shortened URL
        url_data = {'shortened_url': self.shortened_url}
        response = self.client.post('/url_shortener/original_url', url_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['original_url'], self.original_url)