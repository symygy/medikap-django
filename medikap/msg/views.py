from django.shortcuts import render
from django.views import generic
from .models import Message
from .forms import InboxMsgForm, NewMsgForm
from django.urls import reverse_lazy
import datetime

class Inbox(generic.View):
	template_name = 'msg/message_list.html'
	form = InboxMsgForm

	def get(self, request):
		inbox_messages = Message.objects.all()
		context = {
			'inbox_messages' : inbox_messages,
			'form' : self.form
		}

		return render(request, self.template_name, context)

class MsgNew(generic.CreateView):
	model = Message
	form_class = NewMsgForm
	template_name_suffix = "_new"
	success_url = reverse_lazy("msg:inbox")

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.nadawca = self.request.user

		obj.data_utworzenia = datetime.date.today()

		obj.save()
		return super().form_valid(form)

# https://stackoverflow.com/questions/42111303/pass-django-variables-between-view-functions
# https://stackoverflow.com/questions/32787838/how-to-pass-data-between-django-views/32787887