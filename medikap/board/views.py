from django.shortcuts import render
from msg.models import Message
from clients.models import Client
from companies.models import Company
from invoices.models import Invoice

# Create your views here.
def board(request):
	template_name = 'board/summary.html'
	last_clients = Client.objects.all().order_by('-id')[:5]
	last_companies = Company.objects.all().order_by('-id')[:5]
	last_invoices = Invoice.objects.all().order_by('-id')[:5]
	context = {
		'last_clients' : last_clients,
		'last_companies' : last_companies,
		'last_invoices' : last_invoices,
	}

	return render(request, template_name, context)

