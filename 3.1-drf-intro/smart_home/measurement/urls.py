from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from measurement.views import SensorAPIList, SensorDetailUpdate, MeasurementSet

# router = routers.SimpleRouter()
# router.register(r'sensor', SenorViewSet)
# router.register(r'measurements', MeasurementViewSet)


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    # path('v1/', include(router.urls)),
    path('v2/sensors', SensorAPIList.as_view()),
    path('v2/sensors/<int:pk>', SensorDetailUpdate.as_view()),
    path('v2/measurements', MeasurementSet.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
