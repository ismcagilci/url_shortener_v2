# url_shortener_api/serializers.py

from rest_framework import serializers
from .models import ShortenedURL

class ShortenedURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = ['original_url', 'shortened_url']
        read_only_fields = ['shortened_url']

class OriginalURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = ['original_url', 'shortened_url']
        read_only_fields = ['original_url']