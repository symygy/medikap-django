from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Company

class CompanyList(generic.View):
    template_name = 'companies/company_list.html'

    def get(self, request):
        all_companies = Company.objects.all()
        context = {
            'all_companies' : all_companies,
        }
        return render(request, self.template_name, context)

class NewCompany(generic.CreateView):
    model = Company
    template_name_suffix = "_new"
    fields = "__all__"
    success_url = reverse_lazy('companies:list')