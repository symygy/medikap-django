from django import template
from invoices.models import ServiceItem, Service, Invoice

register = template.Library()

@register.simple_tag(takes_context=True)
def service_items_quantity(context):
	request = context['invoice']




	return ServiceItem.objects.all().filter(faktura=request).count()
