from django.db import models

# Create your models here.

class ShortenedURL(models.Model):
    original_url = models.CharField(max_length=200,null=True)
    shortened_url = models.CharField(max_length=100, null=True)