from django.db import models
from companies.models import Company
from django.utils import timezone

class Service(models.Model):
	nazwa = models.CharField(max_length=100)
	cena = models.IntegerField()

	def __str__(self):
		return f'{self.nazwa} - cena: {self.cena}zł'

class Invoice(models.Model):
	forma_platnosci_wybor = [
		('przelew', 'przelew'),
		('gotowka', 'gotówka')
	]

	numer = models.CharField(max_length=30)
	firma = models.ForeignKey(Company, on_delete=models.CASCADE)
	forma_platnosci = models.CharField(verbose_name='forma płatności', max_length=75, choices=forma_platnosci_wybor)
	data_badania = models.DateField()
	data_wystawienia_faktury = models.DateTimeField()
	usluga = models.ManyToManyField(Service, verbose_name='usługi')
	rabat = models.IntegerField(verbose_name='rabat [%]', blank=True, null=True)
	wartosc = models.FloatField(null=True, blank=True)

	def __str__(self):
		return self.numer

	def calculate_total_value(self):
		if self.rabat != 0:
			self.wartosc = 0