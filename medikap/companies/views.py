from django.shortcuts import render, get_object_or_404, redirect,HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Company, File
from .forms import CompanyListForm, UploadFileForm, DetailForm
from clients.models import Client
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

class CompanyList(generic.View):
    template_name = 'companies/company_list.html'
    form = CompanyListForm

    def get(self, request):
        all_companies = Company.objects.all().order_by('nazwa')
        context = {
            'form' : self.form,
            'all_companies' : all_companies,
        }
        return render(request, self.template_name, context)

class NewCompany(generic.CreateView):
    model = Company
    template_name_suffix = "_new"
    fields = "__all__"
    success_url = reverse_lazy('companies:list')

class DetailsCompany(generic.View):
    template_name = 'companies/company_detail.html'
    form_class = DetailForm
    success_url = reverse_lazy("companies:list")

    def get(self, request, company_id):
        employee_list = Client.objects.all().filter(pracodawca=company_id).order_by('data_waznosci_badania')
        file_list = File.objects.all().filter(firma=company_id).order_by('-data_dodania')
        detailed_company = get_object_or_404(Company, id=company_id)
        form = self.form_class(instance=detailed_company)

        context = {
            'form': form,
            'detailed_company': detailed_company,
            'employee_list' : employee_list,
            'file_list' : file_list
        }
        return render(request, self.template_name, context)

    def post(self, request, company_id):
        detailed_company = get_object_or_404(Company, id=company_id)
        form = self.form_class(request.POST, instance=detailed_company)

        if 'update-data' in request.POST and form.is_valid():
            form.save()
            messages.success(request, 'Pomyślnie zaktualizowano dane firmy')
            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

        if request.is_ajax():
            uploaded_file = request.FILES['document']
            file = File(firma=detailed_company, plik=uploaded_file)
            file.save()
            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

        else:
            messages.error(request, 'Coś poszło nie tak. Twoje ostatnie działanie mogło nie zostać przetworzone poprawnie.')
            return redirect('companies:list')

def delete_file(request, pk):
    if request.method == 'POST':
        obj = File.objects.get(pk=pk)
        obj.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

#
# class UploadFile(generic.View):
#     template_name = 'companies/file_new.html'
#
#     def get(self, request):
#         files = File.objects.all()
#         return render(request, self.template_name, { 'files' : files })
#
#     def post(self, request):
#         form = UploadFileForm(self.request.POST, self.request.FILES)
#         if form.is_valid():
#             files = form.save()
#             data = {
#                 'is_valid' : True,
#                 'name' : files.plik.name,
#                 'url' : files.plik.url
#             }
#         else:
#             data = {'is_valid' : False}
#
#         return JsonResponse(data)

class UploadFile(generic.View):
    template_name = 'companies/file_new.html'
    success_url = reverse_lazy("companies:list")
    form = UploadFileForm

    def get(self, request):
        context = {
            'form' : self.form,
        }
        return render(request, self.template_name, context)

