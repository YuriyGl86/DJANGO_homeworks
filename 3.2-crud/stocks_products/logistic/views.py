from django.db.models import Q
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        search = self.request.GET.get('search')
        if search:
            qw_set = Product.objects.filter(Q(title__icontains=search) | Q(description__icontains=search))
            return qw_set

        if not pk:
            return Product.objects.all()

        return Product.objects.filter(pk=pk)


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
