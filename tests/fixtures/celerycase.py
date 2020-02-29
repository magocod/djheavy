"""
...
"""

# third-party
from celery.contrib.testing.worker import start_worker

# Django
from django.test import TransactionTestCase

# local Django
from djheavy import celery_app


class CeleryWorkerTestCase(TransactionTestCase):
    """
    ...
    """

    allow_database_queries = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.celery_worker = start_worker(celery_app)
        cls.celery_worker.__enter__()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.celery_worker.__exit__(None, None, None)
