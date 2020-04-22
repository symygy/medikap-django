from django.urls import path
from . import views

app_name = 'msg'

urlpatterns = [
	path('inbox', views.Inbox.as_view(), name='inbox'),
	path('reply', views.MsgNew.as_view(), name='reply'),
]
