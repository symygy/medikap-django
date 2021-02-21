from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from .models import Invoice, ServiceItem
from .forms import InvoiceListForm, NewInvoiceForm, DetailInvoiceForm
from datetime import datetime, timedelta
from django.http import HttpResponse
from medikap.utils import render_to_pdf
from django.contrib import messages
from services.models import Service



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
	now = datetime.now()

	def next_invoice_number(self):
		year = self.now.strftime("%Y")
		month = self.now.strftime("%m")
		last_invoice = Invoice.objects.all().last()
		if last_invoice is not None:
			last_invoice_number = last_invoice.numer.split("/")
			if last_invoice_number[1] == month:
				new_invoice_number = int(last_invoice_number[0]) + 1
			else:
				new_invoice_number = 1
		else:
			new_invoice_number = 1

		return str(new_invoice_number) + '/' + str(month) + '/' + str(year)

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
			obj.numer = self.next_invoice_number()
			obj.data_wystawienia_faktury = self.now
			obj.save()

			services_counter = 0

			for service in all_services:
				quantity_input = request.POST.get('quantity-'+str(services_counter))
				discount_input = request.POST.get('discount-'+str(services_counter))

				services_counter += 1 #used for proper quality_input recognition

				if int(quantity_input) > 0:
					newServiceItem = ServiceItem(usluga=service, faktura=obj, ilosc=quantity_input, rabat=discount_input)
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

	def get_current_inoice(self, invoice_id):
		return get_object_or_404(Invoice, id=invoice_id)

	def get_all_service_items(self, current_invoice):
		return ServiceItem.objects.all().filter(faktura = current_invoice).order_by('usluga')

	def get_total_invoice_value(self, all_service_items):
		return sum(service_item.get_total_value for service_item in all_service_items)

	def get_invoice_discounted_value(self, all_service_items):
		return sum(service_item.get_discounted_value for service_item in all_service_items)

	def invoice_payment_deadline(self, current_invoice):
		if current_invoice.termin_platnosci != None:
			return current_invoice.data_wystawienia_faktury + timedelta(days=current_invoice.termin_platnosci)


	def get(self, request, invoice_id):
		current_invoice = self.get_current_inoice(invoice_id)
		form = self.form_class(instance=current_invoice)
		request.session['invoice_id'] = current_invoice.id

		all_service_items = self.get_all_service_items(current_invoice)

		context = {
			'invoice': current_invoice,
			'form' : form,
			'services' : Service.objects.all(),
			'services_items' : all_service_items,
			'total_value': self.get_total_invoice_value(all_service_items),
			'total_discounted_value': self.get_invoice_discounted_value(all_service_items),
			'payment_deadline': self.invoice_payment_deadline(current_invoice),
		}

		return render(request, self.template_name, context)

	def post(self, request, invoice_id):
		current_invoice = self.get_current_inoice(invoice_id)
		form = self.form_class(request.POST, instance=current_invoice)

		all_service_items = self.get_all_service_items(current_invoice)

		context = {
			'invoice' : current_invoice,
			'services_items': all_service_items,
			'total_value' : self.get_total_invoice_value(all_service_items),
			'total_discounted_value' : self.get_invoice_discounted_value(all_service_items),
			'payment_deadline': self.invoice_payment_deadline(current_invoice),
		}

		pdf = render_to_pdf('invoices/invoice.html', context)
		services_assigned_to_invoice = current_invoice.uslugi.all()

		if 'update-data' in request.POST and form.is_valid():
			for service in all_service_items:
				service_item = get_object_or_404(ServiceItem, id=service.id)
				quantity_input = request.POST.get('quantity-' + str(service.id))
				discount_input = request.POST.get('discount-' + str(service.id))

				service_item.ilosc = int(quantity_input)
				service_item.rabat = int(discount_input)
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
			messages.error(request, 'Coś poszło nie tak. Twoje ostatnie działanie mogło nie zostać przetworzone poprawnie.')
			return redirect('invoices:list')

class DeleteInvoice(generic.DeleteView):
	model = Invoice
	template_name_suffix = "_delete"
	success_url = reverse_lazy('invoices:list')













