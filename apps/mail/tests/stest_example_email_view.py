# local Django
from tests.fixtures.appcase import InstanceAppTestCase


class EmailRequestTestCase(InstanceAppTestCase):
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
