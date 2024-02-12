
# Create your views here.

from rest_framework import generics
from .serializers import ShortenedURLSerializer, OriginalURLSerializer
from .models import ShortenedURL
from rest_framework.response import Response
from rest_framework.views import APIView
import pyshorteners

class ShortenerURLAPIView(generics.ListCreateAPIView):
    # I have used ListCreateAPIView to create and list the shortened URLs
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer

    def perform_create(self, serializer):
        original_url = serializer.validated_data['original_url']
        shortened_url = pyshorteners.Shortener().tinyurl.short(original_url)
        serializer.save(shortened_url=shortened_url)


class OriginalURLAPIView(APIView):
    # I have used APIView to get the original URL from the shortened URL
    # We should send the shortened URL in the request body
    def post(self, request):
        serializer = OriginalURLSerializer(data=request.data)
        if serializer.is_valid():
            shortened_url = ShortenedURL.objects.filter(shortened_url=serializer.data['shortened_url']).first()
            if shortened_url:
                return Response({'original_url': shortened_url.original_url})
            return Response({'error': 'Shortened URL not found'}, status=404)
        return Response(serializer.errors, status=400)