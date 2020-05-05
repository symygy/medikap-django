from django import forms
from .models import Company, File


class CompanyListForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['nazwa', 'nip', 'regon', 'ulica', 'miasto', 'kod_pocztowy']

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['plik',]

class DetailForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'