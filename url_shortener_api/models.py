from django.db import models

# Create your models here.

class ShortenedURL(models.Model):
    original_url = models.URLField(max_length=700)
    shortened_url_value = models.CharField(max_length=10, null=True, unique=True)

    def __str__(self):
        return self.original_url
