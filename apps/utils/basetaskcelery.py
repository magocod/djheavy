"""
Base tasks celery
"""

# third-party
import celery

# from celery.exceptions import Ignore


class VerifyTaskBase(celery.Task):
    """
    ...
    """

    def on_success(self, retval, task_id, args, kwargs):
        """
        ...
        """

        # print('success', task_id)
        pass

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        """
        ...
        """

        # print(task_id, exc)
        pass
