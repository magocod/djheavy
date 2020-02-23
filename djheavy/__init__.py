from __future__ import absolute_import, unicode_literals

# la aplicación de Celery se creé siempre
# que Django se inicie.
from .celery import app as celery_app

__all__ = ('celery_app',)
