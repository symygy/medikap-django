from django import forms
from .models import Client


class DateInput(forms.DateInput):
	input_type = 'date'

class ClientsTabularList(forms.ModelForm):
	class Meta:
		model = Client
		fields = '__all__'
		exclude = ['komentarz']

class ClientDatePicker(forms.ModelForm):
	class Meta:
		model = Client
		fields = "__all__"
		widgets = {
			'data_badania': DateInput(),
			'data_waznosci_badania': DateInput(),
		}
