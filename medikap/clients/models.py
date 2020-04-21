from django.db import models

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
	numer_telefonu = models.CharField("numer telefonu", max_length=20)
	email = models.CharField("adres e-mail", max_length=50)
	nr_rejestr = models.CharField("numer w rejestrze", max_length=20)
	data_badania = models.DateField("data badania")
	data_waznosci_badania = models.DateField("data upływu badania")
	podstawa_prawna = models.CharField("podstawa prawna", max_length=50, choices=podstawa_prawna_wybor)
	badany_60 = models.BooleanField("badany ukończył 60 rok życia", default=False)
	komentarz = models.TextField("komentarz", blank=True)

