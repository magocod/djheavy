# local Django
from tests.fixtures.appcase import HttpClientTestCase


class SignupEmailTestCase(HttpClientTestCase):
    """
    ...
    """

    def test_request_signup_email_success(self):
        """
        ...
        """

        response = self.public_client.post(
            "/api/email/sign_up/", {"username": "username", "email": "email"}
        )
        # print(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            "We have sent you an email, "
            + "please confirm your email address to complete registration",
        )
