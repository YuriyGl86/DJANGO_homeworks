# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import viewsets, mixins, generics
from rest_framework.viewsets import GenericViewSet

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


#
#
# class MeasurementViewSet(viewsets.ModelViewSet):
#     queryset = Measurement.objects.all()
#     serializer_class = MeasurementSerializer

#
# class SenorViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer


class SensorAPIList(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementSet(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
