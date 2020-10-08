"""
...
"""

from django.test import TestCase

from rest_framework.test import APIClient


class HttpClientTestCase(TestCase):
    """
    ...
    """

    def setUp(self):
        """
        ...
        """

        self.set_http_clients()

    def set_http_clients(self):
        """
        ...
        """
        self.public_client = APIClient()


class InstanceAppTestCase(HttpClientTestCase):
    """
    ...
    """

    def setUp(self):
        """
        ...
        """

        self.set_http_clients()
        # other
