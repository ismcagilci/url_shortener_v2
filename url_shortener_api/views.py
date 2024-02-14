
# Create your views here.

from .serializers import ShortenedURLSerializer
from .models import ShortenedURL
from rest_framework.response import Response
from rest_framework.views import APIView
import hashlib
from rest_framework.generics import get_object_or_404
import os



class ShortenerUrlListCreateDestroyAPIView(APIView):
    """
    List all shortened URLs and create a new shortened URL
    """
    def get(self, request):
        shortened_urls = ShortenedURL.objects.all()
        serializer = ShortenedURLSerializer(shortened_urls, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShortenedURLSerializer(data=self.request.data)
        if serializer.is_valid():
            # Generate MD5 hash of the original URL and take the first 6 characters of the hash
            original_url = serializer.validated_data['original_url']
            check_original_url = ShortenedURL.objects.filter(original_url=original_url).first()
            if check_original_url:
                return Response({"error": "You already shortened same URL before"}, status=400)
            hash_object = hashlib.md5(original_url.encode())
            hash_value = hash_object.hexdigest()[:6].upper()
            serializer.save(shortened_url_value=hash_value)
            url_shortener_key = os.environ.get('URL_SHORTENER_KEY')
            return Response({"shortened_url": f"{url_shortener_key}/{hash_value}"}, status=201)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request):
        ShortenedURL.objects.all().delete()
        return Response(status=204)


class OriginalUrlGetDestroyAPIView(APIView):
    """
    Get and delete the original URL
    """
    def get(self, request, shortened_url_value):
        shortened_url_object = get_object_or_404(ShortenedURL, shortened_url_value = shortened_url_value)
        serializer = ShortenedURLSerializer(shortened_url_object)
        return Response({"original_url": serializer.data.get("original_url")}, status=200)
    def delete(self, request, shortened_url_value):
        shortened_url_object = get_object_or_404(ShortenedURL, shortened_url_value = shortened_url_value)
        shortened_url_object.delete()
        return Response(status=204)