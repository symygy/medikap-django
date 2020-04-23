from django.urls import path, re_path
from . import views

app_name = 'msg'

urlpatterns = [
	path('inbox', views.Inbox.as_view(), name='inbox'),
	path('new', views.NewMessage.as_view(), name='new'),
	re_path(r'^reply/(?P<msg_id>\d+)', views.ReplyMessage.as_view(), name='reply'),
]
