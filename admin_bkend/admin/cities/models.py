from django.db import models


class WeatherData(models.Model):
    temp = models.PositiveIntegerField(default=0)
    wind_speed = models.FloatField(default=0)
    pressure = models.PositiveIntegerField(default=0)


class Cities(models.Model):
    name = models.CharField(max_length=200)
