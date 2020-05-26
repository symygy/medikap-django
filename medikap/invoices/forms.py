from django import forms
from .models import Invoice

class DateInput(forms.DateInput):
	input_type = 'date'

class InvoiceListForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = '__all__'
		exclude = ['usluga', 'data_badania', 'rabat']

class NewInvoiceForm(forms.ModelForm):
	# def clean_region(self):
	# 	if len(self.cleaned_data['region']) > 1:
	# 		raise forms.ValidationError('Select only 1 option.')
	# 	return self.cleaned_data['region']

	class Meta:
		model = Invoice
		fields = '__all__'
		exclude = ['numer', 'data_wystawienia_faktury']
		widgets = {
			'usluga' : forms.CheckboxSelectMultiple,
			'data_badania' : DateInput(),
		}