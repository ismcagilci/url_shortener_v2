from django.urls import path
from url_shortener_api import views

urlpatterns = [
    path("", views.ShortenerURLAPIView.as_view(), name="create_shortened_url_api_view"),
    path("original_url", views.OriginalURLAPIView.as_view(), name="get_original_url_api_view"),
]