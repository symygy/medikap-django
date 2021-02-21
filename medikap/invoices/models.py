from django.db import models
from companies.models import Company
from services.models import Service
from clients.models import Client
from datetime import datetime, timedelta

class Invoice(models.Model):
	forma_platnosci_wybor = [
		('przelew', 'przelew'),
		('gotowka', 'gotówka')
	]

	termin_platnosci_wybor = [
		(0, 'dzisiaj'),
		(7, '7 dni'),
		(14, '14 dni'),
		(21, '21 dni')
	]

	numer = models.CharField(max_length=30)
	firma = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
	osoba_prywatna = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
	forma_platnosci = models.CharField(verbose_name='forma płatności', max_length=75, choices=forma_platnosci_wybor)
	data_badania = models.DateField()
	data_wystawienia_faktury = models.DateTimeField()
	termin_platnosci = models.IntegerField(verbose_name='termin płatności', default=termin_platnosci_wybor[0][0], blank=True, null=True, choices=termin_platnosci_wybor)
	uslugi = models.ManyToManyField(Service, verbose_name='usługi')

	def __str__(self):
		return self.numer

class ServiceItem(models.Model):
	usluga = models.ForeignKey(Service, on_delete=models.CASCADE)
	faktura = models.ForeignKey(Invoice, on_delete=models.CASCADE)
	ilosc = models.PositiveIntegerField(default=1)
	rabat = models.IntegerField(verbose_name='rabat [%]', blank=True, null=True, default=0)

	def __str__(self):
		return f'{self.usluga.nazwa} [faktura: {self.faktura}]'

	@property
	def get_total_value(self):
		total_value = self.usluga.cena * self.ilosc
		return total_value

	@property
	def get_discounted_value(self):
		discounted_value = (self.usluga.cena - (self.usluga.cena * self.rabat / 100)) * self.ilosc
		return discounted_value


