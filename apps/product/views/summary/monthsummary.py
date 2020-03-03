import calendar
import json

# from typing import Dict, Tuple

# third-party
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from django.db.models import Count
from django.conf import settings
# from django.http import JsonResponse


from django.views.decorators.csrf import csrf_exempt

# from apps.product.models import Product


@api_view(["POST"])
def ProdMonthSummaryView(request):
    """
    ...
    """

    # json_data = json.loads(request.body.decode("utf-8"))
    # print(json_data)

    # COUNT

    total_count: int = 0

    # MONTHS

    weeks, days = calendar.monthrange(2020, 2)
    # print(weeks, days)

    month_summary = []

    for day_number in range(days):
        # print(day_number + 1)
        month_summary.append({"day_number": day_number + 1, "count": 0})

    return Response({"total": total_count, "month_summary": month_summary,}, status=status.HTTP_200_OK)
