from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Django options for celery application.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djheavy.settings")

# Create the Celery application
app = Celery("tasks")

# We specify that Celery configuration variables are found
# in the `settings.py` file of Django.
# The namespace parameter is to say that the configuration variables of
# The celery in the configuration file begins with the prefix * CELERY_ *
app.config_from_object("django.conf:settings", namespace="CELERY")

# This method automatically records the tasks for the broker.
# Search for tasks within all `task.py` files in applications
# and send them to Redis automatically.
app.autodiscover_tasks()

# app.conf.update(
#       BROKER_URL='redis://localhost:6379/0',
# )


@app.task(name="celery.ping")
def ping():  # pragma: no cover
    """
    ignore connection validation with task server (celery)
    """

    # type: () -> str
    """Simple task that just returns 'pong'."""
    return "pong"
