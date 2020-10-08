"""
...
"""

import binascii
import os
import time

# standard library
import pytest

# Django
from django.core.cache import cache

# local Django
from tests.fixtures.appcase import HttpClientTestCase

# from django.test import TestCase

pytestmark = [pytest.mark.unittest]


class ActivateAccountLinkTestCase(HttpClientTestCase):
    """
    ...
    """

    def test_activate_account_link_valid_token(self):
        """
        ...
        """

        username = "usertest"
        email = "emailsuccestest@gmail.com"
        token = binascii.hexlify(os.urandom(20)).decode()

        cache.set(token, f"{username}_{email}_{token}", 30)

        response = self.public_client.post(f"/api/activate/{token}/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, "Your account has been activate successfully")

    def test_activate_account_link_invalid_token(self):
        """
        ...
        """

        username = "usertest"
        email = "emailinvalidtest@gmail.com"
        token = binascii.hexlify(os.urandom(20)).decode()

        cache.set(token, f"{username}_{email}_{token}", 30)

        response = self.public_client.post("/api/activate/invalid/")

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, "Activation link is invalid!")

    def test_activate_account_link_expired_token(self):
        """
        ...
        """

        username = "usertest"
        email = "emailexpiredtest@gmail.com"
        token = binascii.hexlify(os.urandom(20)).decode()

        cache.set(token, f"{username}_{email}_{token}", 1)

        time.sleep(2)
        response = self.public_client.post(f"/api/activate/{token}/")

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, "Activation link is invalid!")

    def test_activate_account_link_no_token(self):
        """
        ...
        """

        response = self.public_client.post("/api/activate/")

        self.assertEqual(response.status_code, 404)

    def test_activate_account_link_blank_token(self):
        """
        ...
        """

        response = self.public_client.post("/api/activate//")

        self.assertEqual(response.status_code, 404)
