from django.db import models

class Service(models.Model):
	nazwa = models.CharField(max_length=100)
	cena = models.FloatField()

	def __str__(self):
		return f'{self.nazwa} - cena: {self.cena}zł'