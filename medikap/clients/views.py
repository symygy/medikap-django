from django.shortcuts import render
from django.views import generic
from .models import Client
from .forms import ClientsTabularList
from django.core import serializers

class ClientList(generic.View):
	template_name = 'clients/client-list.html'
	context_object_name = 'all_clients'
	form = ClientsTabularList
	all_clients = Client.objects.all()

	def get(self, request):
		context = {
			'form' : self.form,
			'all_clients' : self.all_clients,
		}

		return render(request, self.template_name, context)