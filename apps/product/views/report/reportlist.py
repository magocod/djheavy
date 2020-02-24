"""
...
"""

# third-party
from rest_framework import generics

# local Django
from apps.product.serializers import ReportProductSerializer
from apps.product.models import ReportProduct


class ReportProductListView(generics.ListAPIView):
    """
    ...
    """

    # queryset = ReportProduct.objects.all()
    serializer_class = ReportProductSerializer

    def get_queryset(self):
        """
        ...
        """

        # print(self.kwargs)
        if self.kwargs['slug'] not in ['D', 'M', 'Y']:
            return []

        return ReportProduct.objects.filter(
            rformat=self.kwargs['slug']
        ).order_by('id')
