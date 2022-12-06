from rest_framework.routers import DefaultRouter

from logistic.views import ProductViewSet, StockViewSet

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')
router.register('stocks', StockViewSet, basename='stock')

urlpatterns = router.urls
