import pytest
# from rest_framework.authtoken.models import Token
# from rest_framework.test import APIClient


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    """
    Cargar bd de prueba
    """
    with django_db_blocker.unblock():
        # call_command("default_db")
        pass


# @pytest.fixture
# def admin_client():
#     """
#     super user
#     """
#     client = APIClient()
#     token, _ = Token.objects.get_or_create(user__username="super_user_admin")
#     client.credentials(HTTP_AUTHORIZATION="Token " + token.key,)
#     return client