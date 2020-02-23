from django.urls import path

from apps.product.views import (
    daysummary, monthsummary, yearsummary
)


urlpatterns = [
    path(
    	'product_summary/d/',
    	daysummary.ProdDaySummaryView,
    	name='product_day_summary'
    ),
    path(
        'product_summary/m/',
        monthsummary.ProdMonthSummaryView,
        name='product_month_summary'
    ),
    path(
        'product_summary/y/',
        yearsummary.ProdYearSummaryView,
        name='product_year_summary'
    ),
]
