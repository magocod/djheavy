# local Django
from tests.fixtures.appcase import HttpClientTestCase


class RequestDayReportTestCase(HttpClientTestCase):
    """
    ...
    """

    def test_request_day_summary_report_success(self):
        """
        ...
        """

        response = self.public_client.post("/api/product_summary/d/", {"text": "data"})
        # print(response)
        self.assertEqual(response.status_code, 200)
