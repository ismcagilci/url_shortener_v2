# Generated by Django 5.0.2 on 2024-02-14 12:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("url_shortener_api", "0005_shortenedurl_shortened_url_value_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="shortenedurl",
            name="shortened_url_key",
        ),
    ]
