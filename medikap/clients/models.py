from django.db import models
from companies.models import Company

class Client(models.Model):
	podstawa_prawna_wybor = [
		('kier_zaw', 'kierowca zawodowy'),
		('kier_uprz', 'kierowca uprzywilejowany'),
		('instr_egz', 'instruktor / egzaminator'),
		('zatrz_pra_jaz', 'zatrzymane prawo jazdy'),
		('inna', 'inna')
	]


	imie = models.CharField("imię", max_length=100)
	nazwisko = models.CharField("nazwisko", max_length=100)
	numer_telefonu = models.CharField("numer telefonu", max_length=20, blank=True, null=True)
	email = models.CharField("adres e-mail", max_length=50, blank=True, null=True)
	nr_rejestr = models.CharField("numer w rejestrze", max_length=20, blank=True, null=True)
	data_badania = models.DateField("data badania", blank=True, null=True)
	data_waznosci_badania = models.DateField("data upływu badania", blank=True, null=True)
	podstawa_prawna = models.CharField("podstawa prawna", max_length=50, choices=podstawa_prawna_wybor, blank=True, null=True)
	komentarz = models.TextField("komentarz", blank=True)
	pracodawca = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return f'{self.nazwisko} {self.imie}'

