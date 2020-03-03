# local Django
from tests.fixtures.appcase import HttpClientTestCase


class RequestYearReportTestCase(HttpClientTestCase):
    """
    ...
    """

    def test_request_year_summary_report_success(self):
        """
        ...
        """

        response = self.public_client.post("/api/product_summary/y/", {"text": "data"})
        # print(response)
        self.assertEqual(response.status_code, 200)
