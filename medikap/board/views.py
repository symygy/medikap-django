from django.shortcuts import render
from msg.models import Message

# Create your views here.
def board(request):
	template_name = 'board/base.html'
	return render(request, template_name)

