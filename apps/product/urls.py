from django.urls import path

from apps.product.views.summary import daysummary, monthsummary, yearsummary
from apps.product.views.report import reportlist

urlpatterns = [
    path(
        "product_summary/d/", daysummary.ProdDaySummaryView, name="product_day_summary"
    ),
    path(
        "product_summary/m/",
        monthsummary.ProdMonthSummaryView,
        name="product_month_summary",
    ),
    path(
        "product_summary/y/",
        yearsummary.ProdYearSummaryView,
        name="product_year_summary",
    ),
    path(
        "report/list/<slug:slug>/",
        reportlist.ReportProductListView.as_view(),
        name="report_prodyct_list",
    ),
]
