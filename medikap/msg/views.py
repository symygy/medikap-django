from django.shortcuts import render, redirect
from django.views import generic
from .models import Message
from .forms import InboxMsgForm, NewMsgForm, ReplyMsgForm
from django.urls import reverse_lazy, reverse
import datetime

class Inbox(generic.View):
	template_name = 'msg/message_list.html'
	form = InboxMsgForm

	def get(self, request):
		inbox_messages = Message.objects.all().filter(odbiorca=self.request.user)
		context = {
			'inbox_messages' : inbox_messages,
			'form' : self.form
		}
		return render(request, self.template_name, context)

class NewMessage(generic.CreateView):
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

class ReplyMessage(generic.View):
	# View can be used to display messages as mootstrap modals
	model = Message
	form_class = ReplyMsgForm
	template_name = 'msg/message_reply.html'
	success_url = reverse_lazy("msg:inbox")

	def get(self, request, msg_id):
		form = self.form_class(None)
		current_msg = Message.objects.get(id=msg_id)
		context = {
			'form' : form,
			'current_msg' : current_msg,
		}
		return render(request, self.template_name, context)

	def post(self, request, msg_id):
		form = self.form_class(request.POST)
		choosen_msg = Message.objects.get(id=msg_id)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.nadawca = self.request.user
			obj.data_utworzenia = datetime.date.today()
			obj.odbiorca = choosen_msg.nadawca
			obj.save()
			return redirect ('msg:inbox')

		return render(request, self.template_name, {'form' : form})

class DeleteMessage(generic.DeleteView):
	model = Message
	template_name_suffix = "_delete"
	success_url = reverse_lazy('msg:inbox')
