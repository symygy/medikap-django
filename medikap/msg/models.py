from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
	temat = models.CharField(max_length=50, default='Brak tematu')
	nadawca = models.ForeignKey(User, related_name="sender", on_delete=models.SET_DEFAULT, default='nieznany_użytkownik')
	odbiorca = models.ForeignKey(User, related_name="receiver", on_delete=models.SET_DEFAULT, default='nieznany_użytkownik')
	wiadomosc = models.TextField("wiadomość")
	data_utworzenia = models.DateField()

