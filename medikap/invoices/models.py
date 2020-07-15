from django.db import models
from companies.models import Company
from django.utils import timezone

class Service(models.Model):
	nazwa = models.CharField(max_length=100)
	cena = models.FloatField()

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
	rabat = models.IntegerField(verbose_name='rabat [%]', blank=True, null=True)
	uslugi = models.ManyToManyField(Service, verbose_name='usługi')

	def __str__(self):
		return self.numer

class ServiceItem(models.Model):
	usluga = models.ForeignKey(Service, on_delete=models.CASCADE)
	faktura = models.ForeignKey(Invoice, on_delete=models.CASCADE)
	ilosc = models.PositiveIntegerField(default=1)

	def __str__(self):
		return f'{self.usluga.nazwa} [faktura: {self.faktura}]'

	@property
	def get_total_value(self):
		total_value = self.usluga.cena * self.ilosc
		return total_value