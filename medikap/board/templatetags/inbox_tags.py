from django import template
from msg.models import Message
from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag(takes_context=True)
def unread_msg_counter(context):
	request = context['user']
	return Message.objects.all().filter(data_odczytania=None).filter(odbiorca=request).count()
