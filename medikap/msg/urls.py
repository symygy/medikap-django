from django.urls import path, re_path
from . import views

app_name = 'msg'

urlpatterns = [
	path('inbox', views.Inbox.as_view(), name='inbox'),
	path('new', views.NewMessage.as_view(), name='new'),
	re_path(r'^detail/(?P<msg_id>\d+)/$', views.ReplyMessage.as_view(), name='reply'),
	re_path(r'^detail/(?P<pk>\d+)/delete', views.DeleteMessage.as_view(), name='delete'),
]
