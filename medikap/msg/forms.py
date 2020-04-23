from django import forms
from .models import Message

class InboxMsgForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = '__all__'
		exclude = ['odbiorca']

class NewMsgForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = ['odbiorca', 'temat', 'wiadomosc']

class ReplyMsgForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = ['temat', 'wiadomosc']
