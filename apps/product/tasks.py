from __future__ import absolute_import, unicode_literals

# standard library
import json
from typing import Any, Dict

# third-party
from celery import shared_task

# local Django
from apps.product.models import ReportProduct


@shared_task
def generate_day_report(request: Dict[str, Any]):
    """
    ...
    """

    # COUNT

    total_count: int = 0

    # DAY

    day_summary = []

    for number in range(24):
        # print(day_number + 1)
        hour = ""

        if len(str(number)) == 2 and number >= 10:
            hour = f"{number}:00:00"
        else:
            hour = f"0{number}:00:00"

        day_summary.append({"hour": hour, "count": 0})

    report = ReportProduct.objects.create(
        rformat="D",
        total=json.dumps({"total_count": total_count}),
        summary=json.dumps({"day_summary": day_summary}),
    )
    report_id = report.id
    return f"day report completed id: {report_id}"
