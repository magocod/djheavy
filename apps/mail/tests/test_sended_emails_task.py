"""
...
"""

# third-party
from celery import states

# Django
from django.db.utils import IntegrityError

# local Django
from apps.mail.models import Mail
from apps.mail.tasks import simulate_send_emails
from tests.fixtures.celerycase import CeleryWorkerTestCase


class EmailTaskTestCase(CeleryWorkerTestCase):
    """
    ...
    """

    def test_simulate_send_emails_task_success(self):
        """
        ...
        """

        email_payload = "test@gmail.com"
        task = simulate_send_emails.delay(email_payload)
        task_result = task.get()
        # print("test db", Mail.objects.count())

        self.assertEqual(task.status, states.SUCCESS)
        self.assertEqual(task_result["sended_to"], email_payload)
        self.assertEqual(1, Mail.objects.count())

    def test_simulate_send_emails_task_failed__error_parameters(self):
        """
        ...
        """
        try:
            email_payload = None
            task = simulate_send_emails.delay(email_payload)
            _ = task.get()
        except Exception as e:
            self.assertEqual(task.status, states.FAILURE)
            self.assertTrue(isinstance(e, IntegrityError))
            self.assertEqual(0, Mail.objects.count())
