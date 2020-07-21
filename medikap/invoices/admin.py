from django.contrib import admin
from .models import Invoice, ServiceItem

admin.site.register(Invoice)
admin.site.register(ServiceItem)
