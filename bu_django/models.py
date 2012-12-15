from django.db import models

class Tester(models.Model):
	email = models.CharField(max_length=30)

class Weather(models.Model):
	city = models.CharField(max_length=30)
        lowest_temperature = models.CharField(max_length=10)
	forecast = models.CharField(max_length=10)
	last_update_time = models.DateField(auto_now=True)
