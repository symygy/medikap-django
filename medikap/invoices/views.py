from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import Invoice
from .forms import InvoiceListForm, NewInvoiceForm
import datetime
from django.http import HttpResponse
from medikap.utils import render_to_pdf, link_callback

class InvoiceList(generic.View):
	template_name = 'invoices/invoice_list.html'
	form = InvoiceListForm

	def get(self, request):
		all_invoices = Invoice.objects.all()
		context = {
			'form': self.form,
			'all_invoices': all_invoices,
		}
		return render(request, self.template_name, context)

class NewInvoice(generic.CreateView):
	model = Invoice
	template_name_suffix = "_new"
	form_class = NewInvoiceForm
	success_url = reverse_lazy('invoices:list')
	now = datetime.datetime.now()
	
	def next_offer_number(self):
		year = self.now.strftime("%Y")
		month = self.now.strftime("%m")
		last_invoice = Invoice.objects.all().last()
		print('--------------------------------------------------')
		print(last_invoice)
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
	
	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.numer = self.next_offer_number()
		obj.data_wystawienia_faktury = self.now
		obj.save()
		return super(NewInvoice, self).form_valid(form)

class DetailsInvoice(generic.View):
	template_name = 'invoices/invoice_detail.html'
	# form_class = DetailForm
	success_url = reverse_lazy("invoices:list")

	def get(self, request, invoice_id):
		invoice = get_object_or_404(Invoice, id=invoice_id)
		context = {
			'invoice': invoice,
		}
		return render(request, self.template_name, context)

	def post(self, request, invoice_id):
		invoice = get_object_or_404(Invoice, id=invoice_id)

		if 'view-pdf' in request.POST:
			pdf = render_to_pdf('invoices/invoice.html', {'invoice' : invoice})
			return HttpResponse(pdf, content_type='application/pdf')
		if 'download-pdf' in request.POST:
			pdf = render_to_pdf('invoices/invoice.html', {'invoice' : invoice})

			response = HttpResponse(pdf, content_type='application/pdf')
			filename = f"Faktura {invoice.numer}.pdf"
			content = "attachment; filename='%s'" % (filename)
			response['Content-Disposition'] = content
			return response
		else:
			# dodać komunikat o błędzie
			return redirect('invoices:list')

class DeleteInvoice(generic.DeleteView):
	model = Invoice
	template_name_suffix = "_delete"
	success_url = reverse_lazy('invoices:list')