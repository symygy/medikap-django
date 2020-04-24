from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
	temat = models.CharField(max_length=50)
	nadawca = models.ForeignKey(User, related_name="sender", on_delete=models.SET_DEFAULT, default='nieznany_użytkownik')
	odbiorca = models.ForeignKey(User, related_name="receiver", on_delete=models.SET_DEFAULT, default='nieznany_użytkownik')
	wiadomosc = models.TextField("wiadomość")
	data_utworzenia = models.DateTimeField()
	data_odczytania = models.DateTimeField(null=True, blank=True)
	data_odpowiedzi = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return f'msg id: {self.id} from: {self.nadawca} to: {self.odbiorca} subject: {self.temat}'

	# https: // github.com / arneb / django - messages