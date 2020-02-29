"""
...
"""

# standard library
# from unittest.mock import patch

# third-party
from celery import states

# local Django
from apps.mail.tasks import example_add

from tests.fixtures.celerycase import CeleryWorkerTestCase


class ExampleTaskTestCase(CeleryWorkerTestCase):
    """
    ...
    """

    # @patch('apps.mail.tasks.example_add')
    def test_example_add_task_success(self):
        """
        ...
        """

        task = example_add.delay(2, 3)
        task_result = task.get()
        self.assertEqual(task.status, states.SUCCESS)
        self.assertEqual(task_result, 5)

    def test_example_add_task_failed__error_parameters(self):
        """
        ...
        """

        with self.assertRaises(TypeError) as raised:
            task = example_add.delay("2", 3)
            task.get()

        # self.assertEqual(
        #     "can only concatenate str (not "int") to str",
        #     str(raised.exception)
        # )
        self.assertEqual(task.status, states.FAILURE)
        self.assertTrue(isinstance(raised.exception, TypeError))
