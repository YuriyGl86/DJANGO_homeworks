from rest_framework import serializers

from measurement.models import Measurement, Sensor


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sens_id', 'temperature', 'measured_at', 'photo']


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', ]


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
