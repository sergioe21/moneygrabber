from __future__ import unicode_literals

from django.db import models
from datetime import date
# Create your models here.
	
class TimeSeries(models.Model):

	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class Price(models.Model):

	price_of = models.ForeignKey('TimeSeries',on_delete=models.CASCADE)
	date = models.DateField(default = date.today)
	price = models.DecimalField(max_digits = 7,decimal_places = 2)

	def __str__(self):

		return str(self.price_of) + ' ' + str(self.date) 



	
