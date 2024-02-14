
# Create your tests here.

from django.test import TestCase
from rest_framework.test import APIClient
import hashlib
import os

class TestShortenedURL(TestCase):
    def setUp(self):
        # Create a test client
        self.client = APIClient()
        original_url_example = 'http://example.com'
        hash_object = hashlib.md5(original_url_example.encode())
        hash_value = hash_object.hexdigest()[:6].upper()
        self.original_url = original_url_example
        self.shortened_url_key = os.environ.get('URL_SHORTENER_KEY')
        self.shortened_url_value = hash_value
        self.shortened_url = f'{self.shortened_url_key}/{self.shortened_url_value}'

    def test_ShortenerUrlListCreateDestroyAPIView(self):
        # Create a shortened URL
        url_data = {'original_url': self.original_url}
        response = self.client.post('', url_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['shortened_url'], self.shortened_url)

        # Get all shortened URLs
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

        # Delete all shortened URLs
        response = self.client.delete('')
        self.assertEqual(response.status_code, 204)


    def test_OriginalUrlGetDestroyAPIView(self):
        # First, create a shortened URL
        url_data = {'original_url': self.original_url}
        response = self.client.post('', url_data, format='json')
        self.assertEqual(response.status_code, 201)

        # Now, get the original URL from the shortened URL value
        response = self.client.get(f'/{self.shortened_url_value}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['original_url'], self.original_url)

        # Now, delete the shortened URL
        response = self.client.delete(f'/{self.shortened_url_value}')
        self.assertEqual(response.status_code, 204)
