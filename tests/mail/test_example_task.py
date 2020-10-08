import pytest
from celery import states

from apps.mail.tasks import example_add

pytestmark = [pytest.mark.celery]


def test_example_add_task_success(celery_app, celery_worker):
    """[summary]

    [description]

    Arguments:
        celery_app {[type]} -- [description]
        celery_worker {[type]} -- [description]
    """
    task = example_add.delay(2, 3)
    task_result = task.get()
    # print(task_result)
    assert task.status == states.SUCCESS
    assert task_result == 5


def test_example_add_task_failed__error_parameters(celery_app, celery_worker):
    """[summary]

    [description]

    Arguments:
        celery_app {[type]} -- [description]
        celery_worker {[type]} -- [description]
    """

    with pytest.raises(TypeError) as excinfo:
        task = example_add.delay("2", 3)
        task.get()

    assert task.status == states.FAILURE
    # print(excinfo.type, excinfo.typename)
    assert excinfo.type == TypeError
    assert str(excinfo.value) == 'can only concatenate str (not "int") to str'
