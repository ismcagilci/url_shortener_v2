from django.urls import path
from url_shortener_api import views

urlpatterns = [
    path("", views.ShortenerUrlListCreateDestroyAPIView.as_view(), name="create_list_shortened_url_api_view"),
    path("<str:shortened_url_value>", views.OriginalUrlGetDestroyAPIView.as_view(), name="get_original_url_api_view"),
]