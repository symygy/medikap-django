from django import template
from invoices.models import ServiceItem, Service, Invoice

register = template.Library()

@register.simple_tag(takes_context=True)
def service_items_quantity(context):
	request = context['invoice']
	all_service_items = context['services_items']
	services = context['services']

	test = list(all_service_items)
	print(test)

	print(services)

	# for service in services:
	# 	print(service)

	# for service_item in all_service_items:
	# 	# print(service_item.usluga)
	# 	# print(services)
	# 	if service_item.usluga not in services:
	# 		list_of_service_items.append('0')
	# 	else:
	# 		list_of_service_items.append(service_item.ilosc)
	#
	# # print(list_of_service_items)
	# return list_of_service_items




