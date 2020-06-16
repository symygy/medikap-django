from django import forms
from .models import *


class DateInput(forms.DateInput):
	input_type = 'date'

class InvoiceListForm(forms.ModelForm):

	class Meta:
		model = Invoice
		fields = '__all__'
		# exclude = ['uslugi', 'data_badania', 'rabat']
		exclude = ['data_badania', 'rabat']

class NewInvoiceForm(forms.ModelForm):
	#quantity = forms.IntegerField()

	class Meta:
		model = Invoice
		fields = '__all__'
		exclude = ['numer', 'data_wystawienia_faktury']
		widgets = {
			#'uslugi' : forms.CheckboxSelectMultiple,
			'data_badania' : DateInput(),
		}

class DetailInvoiceForm(forms.ModelForm):

	class Meta:
		model = Invoice
		fields = '__all__'
		widgets = {
			'uslugi': forms.CheckboxSelectMultiple,
		}

