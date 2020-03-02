"""
...
"""

# third-party
from celery import states

# Django
from django.core.cache import cache

# local Django
from apps.mail.tasks import send_email_activation

from tests.fixtures.celerycase import CeleryWorkerTestCase


class ActivationEmailTaskTestCase(CeleryWorkerTestCase):
    """
    ...
    """

    def test_simulate_send_emails_task_success(self):
        """
        ...
        """

        username = "usertest"
        email = "test@gmail.com"
        domain = "http://localhost:8000"
        task = send_email_activation.delay(username, email, domain)
        task_result = task.get()
        cache_token = cache.get(task_result)

        self.assertEqual(task.status, states.SUCCESS)
        self.assertNotEqual(None, cache_token)

        tkusername, tkemail, tk = cache_token.split("_")
        self.assertEqual(tkusername, username)
        self.assertEqual(tkemail, email)
        self.assertEqual(tk, task_result)
