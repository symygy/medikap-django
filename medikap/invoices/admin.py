from django.contrib import admin
from .models import Invoice, Service, ServiceItem

admin.site.register(Invoice)
admin.site.register(Service)
admin.site.register(ServiceItem)
