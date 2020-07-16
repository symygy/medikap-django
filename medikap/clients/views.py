from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Client
from .forms import ClientsTabularList, ClientDatePicker
import datetime

class ClientList(generic.View):
	template_name = 'clients/client_list.html'
	form = ClientsTabularList

	def get(self, request):
		# wazne by ponizsze query bylo wewnatrz metody get bo inaczej widok listy nie bedzie sie aktualizował po reverse_lazy
		all_clients = Client.objects.all().order_by('nazwisko')
		context = {
			'form' : self.form,
			'all_clients' : all_clients,
		}
		return render(request, self.template_name, context)

class UpdateClient(generic.UpdateView):
	model = Client
	template_name_suffix = "_update"
	fields = '__all__'
	success_url = reverse_lazy('clients:list')

class DeleteClient(generic.DeleteView):
	model = Client
	template_name_suffix = "_delete"
	success_url = reverse_lazy('clients:list')

class NewClient(generic.CreateView):
	model = Client
	form_class = ClientDatePicker
	template_name_suffix = "_new"
	success_url = reverse_lazy('clients:list')
