from django.db import models

def get_upload_folder_name(instance, filename):
    return f'company_files/nip_{instance.nip}/{filename}'

class Company(models.Model):
    nazwa = models.CharField(verbose_name='Nazwa', max_length=50)
    miasto = models.CharField(max_length=50)
    ulica = models.CharField(max_length=50)
    kod_pocztowy = models.CharField(max_length=50)
    nip = models.CharField(verbose_name='NIP', max_length=50)
    regon = models.CharField(verbose_name='REGON', max_length=50)
    pliki_firmy = models.FileField(verbose_name='Pliki', upload_to=get_upload_folder_name, blank=True)

    def __str__(self):
        return f'{self.nazwa} (NIP: {self.nip})'


