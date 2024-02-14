# url_shortener_api/serializers.py

from rest_framework import serializers
from .models import ShortenedURL

class ShortenedURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = '__all__'
        read_only_fields = ['shortened_url_key']