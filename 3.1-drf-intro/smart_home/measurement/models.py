from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['pk']


class Measurement(models.Model):
    sens_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    measured_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
