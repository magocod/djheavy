import pytest

# local Django
from tests.fixtures.appcase import HttpClientTestCase

pytestmark = [pytest.mark.unittest]


class EmailRequestTestCase(HttpClientTestCase):
    """
    ...
    """

    def test_request_task_send_emails_success(self):
        """
        ...
        """

        response = self.public_client.post("/api/send_emails/", {"text": "data"})
        # print(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, "Emails sended using Celery")
