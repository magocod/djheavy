# local Django
from tests.fixtures import InstanceAppTestCase
from apps.product.models import Product
from apps.product_type.models import ProductType


class ReportProductListTestCase(InstanceAppTestCase):
    """
    ...
    """

    def test_list_reports_by_type_of_format(self):
        """
        ...
        """

        response = self.public_client.get("/api/report/list/D/")

        self.assertEqual(response.status_code, 200)
        self.assertTrue("count" in response.data)
        self.assertTrue("results" in response.data)

    def test_list_reports_format_type_error(self):
        """
        ...
        """

        response = self.public_client.get("/api/report/list/e/")

        self.assertEqual(response.status_code, 200)
        self.assertTrue("results" in response.data)
        self.assertTrue(response.data["count"] == 0)
        self.assertTrue(len(response.data["results"]) == 0)

    def test_report_list_format_type_not_specified(self):
        """
        ...
        """

        response = self.public_client.get("/api/report/list/")

        self.assertEqual(response.status_code, 404)

    def test_list_of_reports_without_parameter_in_url(self):
        """
        ...
        """

        response = self.public_client.get("/api/report/list//")

        self.assertEqual(response.status_code, 404)
