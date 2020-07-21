from django import forms
from invoices.models import Service



class ServiceListForm(forms.ModelForm):

	class Meta:
		model = Service
		fields = '__all__'
