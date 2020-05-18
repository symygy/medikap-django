from django.shortcuts import render
from msg.models import Message
from clients.models import Client
from companies.models import Company

# Create your views here.
def board(request):
	template_name = 'board/summary.html'
	last_clients = Client.objects.all().order_by('-id')[:5]
	last_companies = Company.objects.all().order_by('-id')[:5]
	context = {
		'last_clients' : last_clients,
		'last_companies' : last_companies,
	}

	return render(request, template_name, context)

