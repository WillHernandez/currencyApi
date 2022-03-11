from unicodedata import decimal
from django.db import models
import datetime

class Currency(models.Model):
	name = models.CharField(("Currency"), max_length=5)
	date = models.DateField(("Date"), default=datetime.date.today)
	USD = models.FloatField(default=00.00)
	EUR = models.FloatField(default=00.00)
	AUD = models.FloatField(default=00.00)
	CAD = models.FloatField(default=00.00)
	MXN = models.FloatField(default=00.00)
	RUB = models.FloatField(default=00.00)
	

