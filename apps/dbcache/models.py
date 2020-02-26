from django.db import models


class DjangoCache(models.Model):
    cache_key = models.CharField(primary_key=True, max_length=255)
    value = models.TextField()
    expires = models.DateTimeField()

    class Meta:
        db_table = "django-cache"
        indexes = [
            models.Index(fields=["expires"], name="django-cache_expires"),
        ]
