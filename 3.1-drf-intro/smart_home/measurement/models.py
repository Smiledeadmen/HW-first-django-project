from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    description = models.CharField(max_length=256, verbose_name='Описание')

    class Meta:
        verbose_name = 'Сенсор'
        verbose_name_plural = 'Сенсоры'

    def __str__(self):
        return self.name

class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')

    class Meta:
        verbose_name = 'Измерения'
        verbose_name_plural = 'Измерения'