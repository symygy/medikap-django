from django.db import models

def get_upload_folder_name(instance, filename):
    return f'company_files/nip_{instance.firma.nip}/{filename}'

class Company(models.Model):
    nazwa = models.CharField(verbose_name='Nazwa', max_length=50)
    miasto = models.CharField(max_length=50)
    ulica = models.CharField(max_length=50)
    kod_pocztowy = models.CharField(max_length=50)
    nip = models.CharField(verbose_name='NIP', max_length=50)
    regon = models.CharField(verbose_name='REGON', max_length=50)

    def __str__(self):
        return f'{self.nazwa} (NIP: {self.nip})'

class File(models.Model):
    firma = models.ForeignKey(Company, on_delete=models.CASCADE)
    plik = models.FileField(verbose_name='Pliki', upload_to=get_upload_folder_name, blank=True)
    data_dodania = models.DateTimeField(auto_now=True)
    #https: // simpleisbetterthancomplex.com / tutorial / 2016 / 11 / 22 / django - multiple - file - upload - using - ajax.html

    def __str__(self):
        return str(self.plik.name.split('/')[2])