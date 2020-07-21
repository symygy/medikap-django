from django.shortcuts import render, HttpResponseRedirect
from invoices.models import Service
from django.views import generic
from django.urls import reverse_lazy
from .forms import ServiceListForm

class ServicesList(generic.View):
	template_name = 'services/service_list.html'
	form = ServiceListForm

	def get(self, request):
		all_services = Service.objects.all().order_by('-id')
		context = {
			'form': self.form,
			'all_services': all_services,
		}
		return render(request, self.template_name, context)

class NewService(generic.CreateView):
	model = Service
	template_name_suffix = "_new"
	fields = "__all__"
	success_url = reverse_lazy('services:list')

def delete_service(request, pk):
	if request.method == 'POST':
		obj = Service.objects.get(pk=pk)
		obj.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))