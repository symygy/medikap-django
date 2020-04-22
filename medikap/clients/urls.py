from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
	path('list', views.ClientList.as_view(), name='list'),
	path('new', views.NewClient.as_view(), name='new'),
	path('update/<int:pk>', views.UpdateClient.as_view(), name='update'),
	path('delete/<int:pk>', views.DeleteClient.as_view(), name='delete'),
]