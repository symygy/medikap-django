from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Message
from .forms import InboxMsgForm, NewMsgForm, ReplyMsgForm
from django.urls import reverse_lazy
import datetime

date_time_today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Inbox(generic.View):
	template_name = 'msg/message_list.html'
	form = InboxMsgForm

	def get(self, request):
		inbox_messages = Message.objects.all().filter(odbiorca=self.request.user).order_by('-data_utworzenia')
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
		obj.data_utworzenia = date_time_today
		obj.save()
		return super().form_valid(form)

# class ReplyMessage(generic.View):
# 	# View can be used to display messages as mootstrap modals
# 	model = Message
# 	form_class = ReplyMsgForm
# 	template_name = 'msg/message_reply.html'
# 	success_url = reverse_lazy("msg:inbox")
#
# 	def get(self, request, msg_id):
# 		form = self.form_class(None)
# 		current_msg = Message.objects.get(id=msg_id)
# 		context = {
# 			'form' : form,
# 			'current_msg' : current_msg,
# 		}
# 		return render(request, self.template_name, context)
#
# 	def post(self, request, msg_id):
# 		form = self.form_class(request.POST)
# 		choosen_msg = Message.objects.get(id=msg_id)
# 		if form.is_valid():
# 			obj = form.save(commit=False)
# 			obj.nadawca = self.request.user
# 			obj.data_utworzenia = datetime.date.today()
# 			obj.odbiorca = choosen_msg.nadawca
# 			obj.save()
# 			return redirect ('msg:inbox')
#
# 		return render(request, self.template_name, {'form' : form})

class ReplyMessage(generic.View):
	model = Message
	form_class = ReplyMsgForm
	template_name = 'msg/message_view.html'
	success_url = reverse_lazy("msg:inbox")

	def get(self, request, msg_id):
		form = self.form_class(None)
		current_msg = get_object_or_404(Message, id=msg_id)

		if current_msg.data_odczytania is None:
			current_msg.data_odczytania = date_time_today
			current_msg.save()

		context = {
			'form': form,
			'current_msg' : current_msg,
		}
		return render(request, self.template_name, context)

	def post(self, request, msg_id):
		form = self.form_class(request.POST)
		current_msg = get_object_or_404(Message, id=msg_id)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.nadawca = self.request.user
			obj.data_utworzenia = date_time_today
			obj.odbiorca = current_msg.nadawca
			obj.save()
			return redirect('msg:inbox')

		return render(request, self.template_name, {'form' : form})

class DeleteMessage(generic.DeleteView):
	model = Message
	template_name_suffix = "_delete"
	success_url = reverse_lazy('msg:inbox')




