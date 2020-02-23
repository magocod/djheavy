import json

# from typing import Dict, Tuple

# from django.db.models import Count
from django.http import JsonResponse


from django.views.decorators.csrf import csrf_exempt

# from apps.product.models import Product


@csrf_exempt
def ProdDaySummaryView(request):
    """
    ...
    """

    json_data = json.loads(request.body.decode("utf-8"))
    print(json_data)

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

    return JsonResponse({"total": total_count, "day_summary": day_summary,})
