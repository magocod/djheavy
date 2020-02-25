import calendar
import json

# from typing import Dict, Tuple

# from django.db.models import Count
from django.http import JsonResponse


from django.views.decorators.csrf import csrf_exempt

# from apps.product.models import Product


@csrf_exempt
def ProdMonthSummaryView(request):
    """
    ...
    """

    json_data = json.loads(request.body.decode("utf-8"))
    print(json_data)

    # COUNT

    total_count: int = 0

    # MONTHS

    weeks, days = calendar.monthrange(2020, 2)
    # print(weeks, days)

    month_summary = []

    for day_number in range(days):
        # print(day_number + 1)
        month_summary.append({"day_number": day_number + 1, "count": 0})

    return JsonResponse({"total": total_count, "month_summary": month_summary,})
