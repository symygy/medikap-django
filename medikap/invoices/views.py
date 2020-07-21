from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from .models import Invoice, ServiceItem
from .forms import InvoiceListForm, NewInvoiceForm, DetailInvoiceForm
import datetime
from django.http import HttpResponse, JsonResponse
from medikap.utils import render_to_pdf
from django.contrib import messages
import json
from services.models import Service
from django.forms import inlineformset_factory


class InvoiceList(generic.View):
	template_name = 'invoices/invoice_list.html'
	form = InvoiceListForm

	def get(self, request):
		all_invoices = Invoice.objects.all().order_by('-id')
		context = {
			'form': self.form,
			'all_invoices': all_invoices,
		}
		return render(request, self.template_name, context)

class NewInvoice(generic.View):
	model = Invoice
	template_name = 'invoices/invoice_new.html'
	form_class = NewInvoiceForm
	success_url = reverse_lazy('invoices:list')
	now = datetime.datetime.now()

	def next_offer_number(self):
		year = self.now.strftime("%Y")
		month = self.now.strftime("%m")
		last_invoice = Invoice.objects.all().last()
		if last_invoice is not None:
			last_invoice_number = last_invoice.numer.split("/")
			if last_invoice_number[1] == month or last_invoice_number[2] == year :
				invoice_number = int(last_invoice_number[0]) + 1
			else:
				invoice_number = 1
		else:
			invoice_number = 1

		new_invoice_number = str(invoice_number) + '/' + str(month) + '/' + str(year)

		return new_invoice_number

	def get(self, request):
		invoice = Invoice()
		form = self.form_class(instance=invoice)
		services = Service.objects.all()

		context = {
			'invoice': invoice,
			'form': form,
			'services' : services,
		}

		return render(request, self.template_name, context)

	def post(self, request):
		form = self.form_class(request.POST)
		all_services = Service.objects.all()

		if form.is_valid():
			obj = form.save(commit=False)
			obj.numer = self.next_offer_number()
			obj.data_wystawienia_faktury = self.now
			obj.save()

			for service in all_services:
				quantity_input = request.POST.get('quantity-'+str(service.id))
				if int(quantity_input) > 0:
					newServiceItem = ServiceItem(usluga=service, faktura=obj, ilosc=quantity_input)
					newServiceItem.save()
					obj.uslugi.add(service)
					obj.save()
			messages.success(request, 'Pomyślnie utworzono nową fakturę o numerze: '+ obj.numer)

			return redirect('invoices:list')

		else:
			messages.error(request, 'Coś poszło nie tak. Twoje ostatnie działanie mogło nie zostać przetworzone poprawnie.')
			return redirect('board:summary')

class DetailsInvoice(generic.View):
	template_name = 'invoices/invoice_detail.html'
	form_class = DetailInvoiceForm
	success_url = reverse_lazy("invoices:list")

	def calculate_total_value(self, obj):
		return 999


	def calculate_discouted_value(self, obj):
		# total_value = self.calculate_total_value(obj)
		# discounted_value = total_value['total'] - (total_value['total']*(obj.rabat/100))
		#service_value = obj.usluga.cena - (obj.usluga.cena*(obj.rabat/100))

		return 100
		#return discounted_value


	def get(self, request, invoice_id):
		current_invoice = get_object_or_404(Invoice, id=invoice_id)
		form = self.form_class(instance=current_invoice)
		request.session['invoice_id'] = current_invoice.id

		services = Service.objects.all()
		all_service_items = ServiceItem.objects.all().filter(faktura = current_invoice).order_by('usluga')

		context = {
			'invoice': current_invoice,
			'form' : form,
			'total_invoice_value' : self.calculate_total_value(current_invoice),
			'discounted_value': self.calculate_discouted_value(current_invoice),

			'services' : services,
			'services_items' : all_service_items,
		}

		return render(request, self.template_name, context)

	def post(self, request, invoice_id):

		current_invoice = get_object_or_404(Invoice, id=invoice_id)
		form = self.form_class(request.POST, instance=current_invoice)

		all_service_items = ServiceItem.objects.all().filter(faktura=current_invoice)

		context = {
			'invoice' : current_invoice,
			'total_invoice_value' : self.calculate_total_value(current_invoice),
			'discounted_value' : self.calculate_discouted_value(current_invoice)
		}

		pdf = render_to_pdf('invoices/invoice.html', context)
		services_assigned_to_invoice = current_invoice.uslugi.all()

		if 'update-data' in request.POST and form.is_valid():
			for service in all_service_items:
				service_item = get_object_or_404(ServiceItem, id=service.id)
				quantity_input = request.POST.get('quantity-' + str(service.id))

				service_item.ilosc = int(quantity_input)
				service_item.save()

			form.save()

			for service_item in all_service_items:
				if service_item.usluga not in services_assigned_to_invoice:
					service_item.delete()

			for single_service in services_assigned_to_invoice:
				new_service_item, created = ServiceItem.objects.get_or_create(usluga=single_service, faktura=current_invoice)

			messages.success(request, 'Pomyślnie zaktualizowane dane')
			return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

		if 'view-pdf' in request.POST:
			return HttpResponse(pdf, content_type='application/pdf')

		if 'download-pdf' in request.POST:
			response = HttpResponse(pdf, content_type='application/pdf')
			filename = f"Faktura {current_invoice.numer}.pdf"
			content = "attachment; filename={}".format(filename)
			response['Content-Disposition'] = content
			return response
		else:
			# dodać komunikat o błędzie
			return redirect('invoices:list')

class DeleteInvoice(generic.DeleteView):
	model = Invoice
	template_name_suffix = "_delete"
	success_url = reverse_lazy('invoices:list')













