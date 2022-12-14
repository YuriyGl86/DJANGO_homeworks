from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductStockAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000



class ProductViewSet(ModelViewSet):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    pagination_class = ProductStockAPIListPagination

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
    # queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    pagination_class = ProductStockAPIListPagination

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        products = self.request.GET.get('products')
        if products:
            qw_set = Stock.objects.filter(positions__product__title__contains=products).distinct()
            return qw_set

        if not pk:
            return Stock.objects.all()

        return Stock.objects.filter(pk=pk)
