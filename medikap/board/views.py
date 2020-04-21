from django.shortcuts import render

# Create your views here.
def board(request):
	template_name = 'board/index.html'
	return render(request, template_name)

