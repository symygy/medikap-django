from django import forms
from .models import Client

class ClientsTabularList(forms.ModelForm):
	class Meta:
		model = Client
		fields = '__all__'
		exclude = ['badany_60', 'komentarz']