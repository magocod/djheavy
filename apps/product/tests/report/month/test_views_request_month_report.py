# local Django
from tests.fixtures.appcase import HttpClientTestCase


class RequestMonthReportTestCase(HttpClientTestCase):
    """
    ...
    """

    def test_request_month_summary_report_success(self):
        """
        ...
        """

        response = self.public_client.post("/api/product_summary/m/", {"text": "data"})
        # print(response)
        self.assertEqual(response.status_code, 200)
